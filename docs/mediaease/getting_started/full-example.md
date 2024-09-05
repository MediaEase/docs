# Full Example

This example demonstrates how to run the `setup.sh` script with various options to configure your environment.

### Example Command

```bash
username="john"
password="superpassword"
email="test@me.com"
ports="4747,5757"
raid="0,ext4,/home,md10"
domain="mediaease.io"
lang="en"
vault_salt="youllneverguessit"
./setup.sh -u $username -p $password -e $email --ports $ports --raid $raid -d $domain --lang $lang -vs $vault_salt --no-lock --no-reboot
```

### Parameter Descriptions

- `username`: The username for the setup. In this example, it's set to **john**.
- `password`: The password for the user. Here, it's set to **superpassword**.
- `email`: The email address associated with the user. This example uses **test@me.com**.
- `ports`: A comma-separated list of ports to be used. In this case, **4747** and **5757**.
- `raid`: RAID configuration settings, which include:
  - RAID level (e.g., **0**)
  - File system type (e.g., **ext4**)
  - Mount point (e.g., **/home**)
  - Device name (e.g., **md10**)  
  [See more about RAID setup](raid-setup.md)
- `domain`: The domain name for your setup. Here, it's **mediaease.io**.
- `lang`: The language setting for the setup. In this example, it's set to **English (en)**.
- `vault_salt`: A salt value for securing your vault. This example uses **youllneverguessit**.
- `branch`: The branch to use for installation. By default, it's **main**, but you can use **beta** to access the latest unstable features.
- `verbose`: Enables detailed logging during the installation.
- `hostname`: Sets the system hostname. In this example, it's **mediaease-server**.
- `bypass_prompt`: Bypasses any interactive prompts during installation.
- `no_lock`: Disables the generation of the Metapackage to lock installed dependencies.
- `no_reboot`: Prevents the system from rebooting at the end of the installation process. Bypasses the reboot prompt.
- `virtual_machine`: Configures the system for a virtual machine environment.
- `reboot`: Force to reboot at the end of the installation. Bypasses the reboot prompt.

### Command Breakdown

- `./setup.sh`: The script to execute.
- `-u $username`: Sets the username.
- `-p $password`: Sets the password.
- `-e $email`: Sets the email address.
- `--ports $ports`: Sets the ports.
- `--raid $raid`: Configures RAID settings.
- `-d $domain`: Sets the domain name.
- `--lang $lang`: Sets the language.
- `-vs $vault_salt`: Sets the vault salt.
- `-b $branch`: Sets the branch for installation (e.g., **main**, **beta**).
- `--verbose`: Enables verbose mode.
- `--no-lock`: Skips the generation of a Metapackage.
- `--no-reboot`: Disables automatic reboot at the end of installation.
- `--bypass-prompt`: Skips prompts that usually require user input.
- `--hostname $hostname`: Configures the system hostname.
- `--vm`: Configures the system for a virtual machine.

### Complete Command Example

```bash
username="john"
password="superpassword"
email="test@me.com"
ports="4747,5757"
raid="0,ext4,/home,md10"
domain="mediaease.io"
lang="en"
vault_salt="youllneverguessit"

./setup.sh -u $username -p $password -e $email --ports $ports --raid $raid -d $domain --lang $lang -vs $vault_salt --no-lock --no-reboot --hostname mediaease-server --bypass-prompt --verbose
```

### Notes

- **Metapackage Generation**: By default, MediaEase will generate a Metapackage to lock installed dependencies. You can skip this by using the `--no-lock` flag if you're confident in your package management.
  
- **Reboot**: MediaEase will prompt you to reboot after the installation. You can skip this with the `--no-reboot` flag, but it’s recommended to reboot to ensure all changes are applied.

### Permissions

Ensure that the `setup.sh` script is executable before running the installation. If not, make it executable with:

```bash
chmod +x setup.sh
```

By following this guide, you can easily customize and execute the `setup.sh` script according to your needs.
