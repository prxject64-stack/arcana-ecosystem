{
  description = "Arcana Sovereign and Credit Coin Private Environment - 2026 Standard";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          buildInputs = with pkgs; [
            nodejs_22
            nodePackages.npm
            git
            python3
          ];

          shellHook = ''
            export PATH="$PWD/node_modules/.bin:$PATH"
            echo "--- ARCANA SOVEREIGN 2026: ENVIRONMENT READY ---"
            echo "Assets: 136B CC (Credit Coin Private) | ARC (Arcana Sovereign)"
          '';
        };
      });
}
