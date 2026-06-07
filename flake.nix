{
  description = "stakeholder-circus center-ring";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      systems = [ "x86_64-linux" "aarch64-darwin" "x86_64-darwin" ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
    in {
      devShells = forAllSystems (system:
        let pkgs = import nixpkgs { inherit system; };
        in {
          default = pkgs.mkShell {
            packages = with pkgs; [ actionlint jq yq-go python312 ];
          };
        });
      apps = forAllSystems (system:
        let pkgs = import nixpkgs { inherit system; };
            mk = name: text: {
              type = "app";
              program = "${pkgs.writeShellScript name text}";
            };
        in {
          build = mk "build" ''echo "center-ring is documentation and workflow focused"'';
          test = mk "test" ''python3 scripts/validate_program_docs.py'';
          check = mk "check" ''actionlint && python3 scripts/validate_program_docs.py'';
          format = mk "format" ''echo "No formatter baseline defined for center-ring"'';
        });
    };
}
