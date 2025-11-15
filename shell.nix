{ pkgs ? import <nixpkgs> {
    config.allowUnfreePredicate = pkg: builtins.elem (pkgs.lib.getName pkg) [
      "1password-cli"
    ];
  }
}:

pkgs.mkShell {
  buildInputs = with pkgs; [
    # Python version and package management
    uv
    
    # 1Password CLI
    _1password-cli
  ];

  # shellHook = ''
  #   uv sync
  #   source .venv/bin/activate
  # '';
}
