
# Google BLock Storage

  - block storage - hard disk storage

  - direct attached storage
    * block storage will be physically and directly attached to your VM or kubernetes engine
    * low latency

  - network attached storage
    * block storage can exist anywhere in a remote location (not attached to your VM/kubernetes engine)

## Directly attached - Local SSD

  - Local SSD

  - physically attached to VM

  - very high performance - 10x to 100x of persistance disk

  - more expensive than persistance disk

  - you can not re attach to other VM

  - if you destroy your VM, the local SSD will be deleted

  - lower availability

  - temporary/Ephemeral storage

  - no snapshots (backup)

## Network attached storage

  - network attached hard disk

  - persistent disks

  - zonal, regional

  - not attached directly to any VM

  - can be re-attached to another VM

  - very flexible - resize easily

  - permanent storage

  - snapshot supported

  - cheaper than local SSD
