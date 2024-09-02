# Choosing a Strong Password

When configuring MediaEase, selecting a secure password is essential to protect your server and data. This guide outlines the criteria and best practices for creating a password that ensures the security of your installation.

## Password Requirements

To maintain a balance between security and usability, MediaEase enforces the following password requirements:

### Length
- **Minimum 6 Characters:** Your password must be at least 6 characters long. While this is the minimum, we recommend using longer passwords when possible for increased security.

### Allowed Characters
- **Permitted Characters:** You can use any combination of uppercase letters (A-Z), lowercase letters (a-z), numbers (0-9) and not-reserved characters such as `-_/\`
- **Forbidden Characters:** The following special characters are **not allowed** in passwords: ```!@#$%^&*()+=<>?[]|~`"```

### Why Are Certain Characters Forbidden?

Certain special characters are restricted in passwords because they are reserved or can cause issues within the Linux ecosystem. These characters are often used for specific functions in command-line operations, scripts, or configuration files. For example:

- **Reserved Characters:** Characters like `!`, `@`, and `|` are frequently used in shell commands for piping, conditional operations, or as special operators. Using these characters in passwords could interfere with how commands are processed, leading to potential security risks or unintended behavior.
- **Compatibility Issues:** Some applications and services may not handle passwords containing these special characters well. This can lead to authentication errors or problems during automated processes, making it challenging to maintain a stable environment.

By restricting these characters, MediaEase ensures compatibility across various tools and applications, reducing the risk of errors during setup and daily operations.

### Practical Tips

- **Use a Mix of Characters:** While special characters are forbidden, make sure to combine uppercase letters, lowercase letters, and numbers for stronger passwords.
- **Avoid Common Words:** Don't use easily guessable words, such as "password", "123456", or any part of your username.
- **Avoid Simple Patterns:** Refrain from using patterns like "abcdef" or "123456".

## Example of Strong Passwords

Here are some examples of strong passwords that meet the MediaEase requirements, with varying lengths for added security:

- `aB3cD9`
- `Xy5w-Z7K2`
- `fJ7xY2Lm3Kr` 

While these examples meet the minimum criteria, consider using a password longer than 6 characters for increased security.

## Handling "Bad" Passwords

If you attempt to use a password that does not meet the above requirements, such as being too short or containing forbidden characters, MediaEase will prompt you to choose another password. This ensures that all users adhere to the security standards necessary to protect the system.

When prompted, review the password guidelines above and create a new password that complies with the requirements. This process helps maintain the security and integrity of your MediaEase installation.

## What is a Salted Password?

A **salted password** refers to a password that has been appended or prepended with a random string of characters, known as a "salt," before being hashed. This technique is used to enhance security by ensuring that even if two users have the same password, their stored password hashes will be different due to the unique salt.

### Use of Salted Passwords in the MediaEase Secure Vault

The **MediaEase Secure Vault** is a critical component of your system, designed for securely storing sensitive data such as application passwords, VPN credentials, and more. The vault is totally unique to each installation, with its content obfuscated to ensure that only you, the system administrator, can access it.

- **User Salt:** Before performing any operations in the Secure Vault, such as revealing a password or updating app credentials, you must provide your user salt. This adds an extra layer of security by ensuring that only authorized users can access sensitive information.
- **Salt Generation:** If the salt is auto-generated during installation (while not using the `-vs` or `--vault-salt` flags), you will see the generated salt only once during the installation process. **Make sure to save it somewhere safe** because the salt cannot be changed later.
- **Master Passwords:** Some "master" passwords within the vault are encrypted in a way that they cannot be decoded, even by the system administrator, for security reasons.
- **Security of the Vault:** The use of salted passwords and obfuscation techniques ensures that the data stored in the Secure Vault remains inaccessible to unauthorized users, protecting your system’s integrity.

## Password Best Practices

To further enhance the security of your password:

- **Use a Unique Password:** Ensure that your MediaEase password is unique and not reused from other accounts.
- **Avoid Personal Information:** Don’t include easily accessible personal information such as your name, birthdate, or username in your password.
- **Change Passwords Regularly:** Periodically updating your password can help mitigate the risk of unauthorized access.

## Summary

By following these guidelines, you ensure that your MediaEase installation remains secure, protecting your data and server from potential threats. Always aim for a balance between complexity and memorability to maintain both security and convenience.
