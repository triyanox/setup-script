import subprocess
import os
import shutil


class SetupBuilder:
    def __init__(self):
        self.home_directory = os.path.expanduser("~")
        self.installation_steps = []
        self.file_copying_steps = []

    def run_command(self, command):
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            exit(1)

    def install_package(self, package_name):
        self.installation_steps.append(f"brew install {package_name}")
        return self

    def copy_file(self, source, destination):
        self.file_copying_steps.append(
            (f"{os.getcwd()}/{source}", destination.replace("~", self.home_directory)))
        return self

    def prompt_user(self):
        print("Please configure Git:")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        self.run_command(f"git config --global user.name \"{name}\"")
        self.run_command(f"git config --global user.email \"{email}\"")
        self.run_command("gh auth login")

    def execute(self):
        print("Setting up development environment...")

        if not shutil.which("brew"):
            self.run_command(
                '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')

        for step in self.installation_steps:
            self.run_command(step)

        for source, destination in self.file_copying_steps:
            try:
                shutil.copyfile(source, destination)
            except FileNotFoundError:
                print(f"File not found: {source}")
                exit(1)

        print("Development environment setup completed.")


if __name__ == "__main__":
    builder = SetupBuilder()
    builder.install_package("git")
    builder.install_package("gh")
    builder.install_package("fish")
    builder.install_package("exa")
    builder.run_command("curl -sS https://starship.rs/install.sh | sh")
    builder.run_command(
        "curl - o - https: // raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash")
    builder.run_command(
        "wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash")
    builder.run_command("nvm install 14")
    builder.run_command("nvm install 16")
    builder.run_command("nvm install 18")
    builder.run_command("nvm install 20")
    builder.run_command("npm install -g yarn")
    builder.run_command("npm install -g pnpm")
    builder.run_command("npm install -g typescript")
    builder.run_command("npm install -g ts-node")
    builder.run_command("npm install -g eslint")
    builder.run_command("npm install -g prettier")
    builder.run_command("curl -fsSL https://bun.sh/install | bash")
    builder.install_package("visual-studio-code")
    builder.install_package("iterm2")
    builder.install_package("docker")
    builder.install_package("docker-compose")
    builder.install_package("azure-cli")
    builder.run_command(
        "cat extensions.txt | xargs -L 1 code --install-extension")
    builder.copy_file("starship.toml", "~/.config/starship.toml")
    builder.copy_file("config.fish", "~/.config/fish/config.fish")
    builder.prompt_user()
    builder.execute()
