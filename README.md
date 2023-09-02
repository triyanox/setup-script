# Development Environment Setup

## Instructions

Follow these steps to set up your development environment:

1. Clone this repository or copy the Python script (`setup.py`) to your local machine.

2. Open a terminal and navigate to the directory where the script is located.

3. Run the Python script using the following command:

   ```bash
   python main.py
   ```

   The script will start setting up your development environment.

4. During the setup process, you will be prompted to configure Git. Enter your name and email as requested.

5. Once the script completes, your development environment setup will be finished.

## Tools Installed

The script will install the following tools and packages:

- Git
- GitHub CLI (gh)
- Fish shell
- Exa (a modern replacement for 'ls')
- Starship (a customizable prompt)
- Node Version Manager (nvm) with Node.js versions 14, 16, 18, and 20
- Yarn package manager
- pnpm package manager
- TypeScript
- ts-node
- ESLint
- Prettier
- Visual Studio Code
- iTerm2
- Docker
- Docker Compose
- Azure CLI
- Visual Studio Code extensions (as listed in `extensions.txt`)

## Configuration Files

The script also copies configuration files to your home directory:

- `starship.toml` for configuring Starship
- `config.fish` for configuring the Fish shell

