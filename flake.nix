{
  description = "A simple text selection keyboard layout switcher";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-24.11";
  };

  outputs = { self, nixpkgs }:
    let
      system = "x86_64-linux";
      pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      packages.${system} = {
        default = pkgs.python3Packages.buildPythonApplication {
          pname = "fleepit";
          version = "7";

          dependencies = [
            pkgs.xclip
            pkgs.xdotool
            pkgs.wl-clipboard
          ];

          src = ./.;

          meta = with pkgs.lib;
            {
              description = "A simple text selection keyboard layout switcher";
              license = licenses.asl20;
              platforms = platforms.linux;
            };
        };
      };
    };
}
