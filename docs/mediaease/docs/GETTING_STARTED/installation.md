# Installation

1. **Switch to the Root User**

    ```bash
    sudo -i
    ```

2. **Download the Installer**
    - Using wget:
  
    ```bash
    wget -qO setup.sh https://raw.githubusercontent.com/MediaEase/MediaEase/develop/setup.sh && chmod +x setup.sh
    ```
    - Using curl:

    ```bash
    curl -sSL https://raw.githubusercontent.com/MediaEase/MediaEase/develop/setup.sh -o setup.sh && chmod +x setup.sh
    ```

3. **Customize Your Installation**

> [!TIP]
> Define your custom variables. The `username`, `password`, and `email` are required.

    ```bash
    username="thomas"
    password="thomas"
    email="test@me.com"
    ```

> [!NOTE]
> All flags are optional. If not provided, you will be prompted for the required information during installation.

4. **Run the Installer**

    To install with the customized settings, use the following command:

    ```bash
    ./setup.sh -u $username -p $password -e $email
    ```

[Continue to Additional Options](additional-options.md)
