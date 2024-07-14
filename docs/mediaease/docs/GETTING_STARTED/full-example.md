
# Full Example

```bash
username="john"
password="superpassword"
email="test@me.com"
ports="4747,5757"
raid="0,ext4,/home,md10"
domain="mediaease.io"
lang="en"
vault_salt="youllneverguessit"
./setup.sh -u $username -p $password -e $email --ports $ports --raid $raid -d $domain --lang $lang -vs $vault_salt
```
