# Additional Options

## Run in Verbose Mode

    Add the `-v` flag for verbose output:

    ```bash
    ./setup.sh -u $username -p $password -e $email -v
    ```

## Bypass Prompts

    Add the `--bypass-prompt` flag to bypass all prompts:

    ```bash
    ./setup.sh -u $username -p $password -e $email --bypass-prompt
    ```

> [!WARNING]
> If `--bypass-prompt` is set without `-vs` or `--vault-salt` flags, a default salt password will be used. Save it securely as you will see it only once. 

> [!TIP]
> The vault salt is used internally for storing some information more securely. You should not need to use it directly unless you know what you are doing.

## Using a Virtual Machine?

    Add the `-vm` or `--virtual-machine` flag:

    ```bash
    ./setup.sh -u $username -p $password -e $email -vm
    ```

## Run with Beta Branch (Unstable)

    Add the `-b beta` flag to use the beta branch:

    ```bash
    ./setup.sh -u $username -p $password -e $email -b beta
    ```

## Set a Domain During Install

    Add the `-d` or `--domain` flag:

    ```bash
    domain="mediaease.io"
    ./setup.sh -u $username -p $password -e $email -d $domain
    ```
> [!TIP]
> Setting a domain during installation can help in configuring SSL and other domain-specific settings automatically.

## Set Up a RAID Array

    Add the `--raid` flag with a comma-separated list. Example configurations:

    - `raid 0,ext4,/opt,md69`
    - `raid 5,btrfs,/home,md20`

    Alternatively, you can use the default `--raid` (with no arguments), which will set up as `raid 0,ext4,/home,md10`.

    ```bash
    ./setup.sh -u $username -p $password -e $email --raid

    # or
    
    raid="10,btrfs,/mnt,md15"
    ./setup.sh -u $username -p $password -e $email --raid $raid
    ```
> [!IMPORTANT]
> Possible RAID levels are 0, 5, 6, 10, depending on the number of available disks. 

> [!IMPORTANT]
> Possible filesystem types are ext4, btrfs, xfs. 

> [!TIP]
> Arguments are not positional, so raid /opt/,0,md69,ext4 can also work!

## Choose a Different Language

    This will change the server language as well as translating CLI (Zen)/GUI (HarmonyUI) into the selected language. Add the `-lang` flag. Supported languages: `en` (default) and `fr`.

    ```bash
    lang="en"
    ./setup.sh -u $username -p $password -e $email --lang $lang
    ```
> [!TIP]
> Changing the language can be particularly useful for non-English speaking users to have a more intuitive interface.

## Change Default SSH/FTP Ports

    By default, MediaEase will set up port 4747 for SSH/SFTP and port 5757 for FTP. You can change the ports with the `-ports` flag and a comma-separated list.

    ```bash
    ports="4747,5757"
    ./setup.sh -u $username -p $password -e $email --ports $ports
    ```

[Continue to Raid Setup Array](raid-setup.md)

