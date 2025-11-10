{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python version and package management
    uv
  ];

  # shellHook = ''
  #   uv sync
  #   source .venv/bin/activate
  # '';
}
