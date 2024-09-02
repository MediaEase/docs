# Variable Validation in MediaEase Setup

During the MediaEase setup process, several critical variables are validated to ensure they meet specific requirements and formats. This validation is crucial to maintain the integrity and security of the system. Below is an explanation of each variable that is checked and why these checks are necessary.

## Variables Checked

### 1. `username`
- **Validation Criteria**:
  - Must not contain any of the following special characters: ```!@#$%^&*()+=<>?[]|~`"```
  - Must be at least 3 characters long.

- **Reason**: 
  - The `username` is an essential identifier for users on the system. Restricting special characters prevents potential issues with system commands and scripts that might not handle such characters well. Ensuring a minimum length of 3 characters helps prevent overly simple or insecure usernames.

### 2. `password`
- **Validation Criteria**:
  - Must not contain any of the following special characters: ```!@#$%^&*()+=<>?[]|~`"```
  - Must be at least 6 characters long.

- **Reason**:
  - The `password` is a critical security element. Similar to usernames, restricting special characters ensures compatibility across various applications and scripts. A minimum length of 6 characters is required to avoid weak passwords that are easily guessable or brute-forced.

### 3. `email`
- **Validation Criteria**:
  - Must follow the standard email format: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

- **Reason**:
  - The `email` address is often used for user communication and account recovery. Validating the format ensures that the provided email address is legitimate and can be used reliably for notifications or password resets.

### 4. `domain`
- **Validation Criteria**:
  - Must follow the format: `^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

- **Reason**:
  - The `domain` is used for setting up web services and ensuring proper routing of network requests. Validating the format ensures that the domain is syntactically correct, preventing potential issues with DNS resolution and service accessibility.

### 5. `hostname`
- **Validation Criteria**:
  - Must contain only valid hostname characters: `^[a-zA-Z0-9._@-]+$`

- **Reason**:
  - The `hostname` is the name assigned to the system within a network. It needs to be compliant with hostname specifications to avoid conflicts or errors in network communications. After validation, the hostname is applied to the system, and relevant configuration files are updated to reflect this change.

## Additional Operations

- **Hostname Configuration**:
  - If the variable being validated is `hostname`, the setup process will also:
    - Set the system's hostname using `hostnamectl`.
    - Update the `/etc/hosts` file to reflect the new hostname, ensuring that local hostname resolution is consistent with the system's network identity.

## Validation Function Overview

The validation function `zen::validate::input()` is responsible for checking whether the input provided for each variable matches the expected format. If the input is invalid, the user will be prompted to enter a correct value before proceeding with the setup. This process ensures that all critical variables are correctly formatted, reducing the risk of errors during or after the installation.
