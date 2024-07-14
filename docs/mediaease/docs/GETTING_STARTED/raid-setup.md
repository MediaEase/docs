# Set Up a RAID Array

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

[Continue to Full Example](full-example.md)
