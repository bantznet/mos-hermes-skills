# MOS API endpoint index (spec 0.1.0, base /api/v1)

GET = read. [mut] = POST/PUT/PATCH. [DEL] = DELETE.


## Authentication (19)

GET    /auth/admin-tokens - Get all admin tokens
POST   /auth/admin-tokens - Create admin token [mut]
GET    /auth/admin-tokens/me - Get current token permissions
DELETE /auth/admin-tokens/{id} - Delete admin token [DEL]
PUT    /auth/admin-tokens/{id}/deactivate - Deactivate admin token [mut]
PUT    /auth/admin-tokens/{id}/permissions - Update admin token permissions [mut]
GET    /auth/firstsetup - Get first setup token
GET    /auth/jwt-settings - Get JWT settings
PUT    /auth/jwt-settings - Update JWT expiry time [mut]
POST   /auth/login - User login [mut]
POST   /auth/logout - User logout [mut]
POST   /auth/mfa - Verify MFA code during login [mut]
DELETE /auth/mfa - Disable MFA [DEL]
POST   /auth/mfa/setup - Setup or confirm MFA [mut]
GET    /auth/profile - Get own user profile
GET    /auth/users - Get users (admin sees all, user sees only themselves)
POST   /auth/users - Create new user (admin only) [mut]
PUT    /auth/users/{id} - Update user (admin can update any user, users can update themselves) [mut]
DELETE /auth/users/{id} - Delete user (admin only) [DEL]

## Cron (14)

GET    /cron - Get all cron jobs
POST   /cron - Create new cron job [mut]
GET    /cron/scripts - List all cron scripts
GET    /cron/scripts/{scriptName} - Get cron script content
PUT    /cron/scripts/{scriptName} - Update cron script content [mut]
DELETE /cron/scripts/{scriptName} - Delete cron script [DEL]
GET    /cron/system - Get system cron jobs
GET    /cron/{identifier} - Get specific cron job
PUT    /cron/{identifier} - Update cron job [mut]
DELETE /cron/{identifier} - Delete cron job [DEL]
POST   /cron/{identifier}/disable - Disable cron job [mut]
POST   /cron/{identifier}/enable - Enable cron job [mut]
POST   /cron/{identifier}/start - Start cron job manually [mut]
POST   /cron/{identifier}/stop - Stop running cron job [mut]

## Disks (26)

GET    /disks - List all disks with partitions
GET    /disks/availablefilesystems - Get available filesystems
GET    /disks/descriptions/orphaned - List orphaned disk descriptions
DELETE /disks/descriptions/orphaned - Delete all orphaned disk descriptions [DEL]
DELETE /disks/descriptions/orphaned/{serial} - Delete a specific orphaned disk description [DEL]
POST   /disks/format - Format disk/device [mut]
POST   /disks/power/manage - Manage disk power settings [mut]
POST   /disks/power/status - Get power status for multiple disks [mut]
POST   /disks/sleep - Sleep multiple disks [mut]
GET    /disks/unassigned - List unassigned disks
POST   /disks/wake - Wake multiple disks [mut]
GET    /disks/zram/ramdisks - Get ZRAM ramdisk devices
PUT    /disks/{device}/description - Set or clear a disk description [mut]
GET    /disks/{device}/iostats - Get disk I/O statistics
POST   /disks/{device}/mount - Mount a disk device [mut]
POST   /disks/{device}/partition - Create partition [mut]
DELETE /disks/{device}/partition/{partitionNumber} - Delete partition [DEL]
GET    /disks/{device}/partitions - Get disk partitions
GET    /disks/{device}/power - Get disk power status
POST   /disks/{device}/preclear/abort - Abort preClear operation [mut]
POST   /disks/{device}/sleep - Put disk to sleep/standby [mut]
GET    /disks/{device}/smart - Get SMART information
POST   /disks/{device}/unmount - Unmount a disk device [mut]
GET    /disks/{device}/usage - Get disk usage statistics
POST   /disks/{device}/wake - Wake disk from standby [mut]
DELETE /disks/{device}/wipe - Wipe entire disk [DEL]

## Disks WebSocket (2)

GET    /disks/websocket/events - Disks WebSocket Events Documentation
GET    /disks/websocket/stats - Get Disks WebSocket monitoring statistics

## Docker (27)

GET    /docker/mos/containers - Get Docker images with update status
POST   /docker/mos/containers - Update Docker container indices [mut]
GET    /docker/mos/containers/calc - Get container image sizes
GET    /docker/mos/containers/{name}/calc - Get a single container image size
POST   /docker/mos/create - Create new container from template [mut]
GET    /docker/mos/groups - Get all container groups
POST   /docker/mos/groups - Create a new container group [mut]
PUT    /docker/mos/groups/order - Update group order/index [mut]
PUT    /docker/mos/groups/{groupId} - Update container group (name, icon, containers) [mut]
DELETE /docker/mos/groups/{groupId} - Delete a container group [DEL]
POST   /docker/mos/groups/{groupId}/restart - Restart all containers in a group [mut]
POST   /docker/mos/groups/{groupId}/start - Start all containers in a group [mut]
POST   /docker/mos/groups/{groupId}/stop - Stop all containers in a group [mut]
POST   /docker/mos/groups/{groupId}/upgrade - Upgrade all containers in a group [mut]
GET    /docker/mos/ports - Get Docker container port bindings
DELETE /docker/mos/remove - Remove container and its template [DEL]
GET    /docker/mos/templates - Get all container templates (installed and removed)
GET    /docker/mos/templates/{name} - Get specific container template
GET    /docker/mos/unusedimages - Get unused Docker images
DELETE /docker/mos/unusedimages - Delete unused Docker images [DEL]
POST   /docker/mos/update_check - Check for Docker updates [mut]
POST   /docker/mos/upgrade - Upgrade containers [mut]
POST   /docker/mos/xml_convert - Convert XML using URL [mut]
GET    /docker/{path} - Docker REST API Proxy (GET)
POST   /docker/{path} - Docker REST API Proxy (POST) [mut]
PUT    /docker/{path} - Docker REST API Proxy (PUT) [mut]
DELETE /docker/{path} - Docker REST API Proxy (DELETE) [DEL]

## Docker Compose (14)

GET    /docker/mos/compose/stacks - Get all compose stacks
POST   /docker/mos/compose/stacks - Create a new compose stack [mut]
GET    /docker/mos/compose/stacks/{name} - Get a specific compose stack
PUT    /docker/mos/compose/stacks/{name} - Update a compose stack [mut]
PATCH  /docker/mos/compose/stacks/{name} - Update stack settings [mut]
DELETE /docker/mos/compose/stacks/{name} - Delete a compose stack [DEL]
POST   /docker/mos/compose/stacks/{name}/pull - Pull images for a compose stack [mut]
POST   /docker/mos/compose/stacks/{name}/restart - Restart a compose stack [mut]
POST   /docker/mos/compose/stacks/{name}/start - Start a compose stack [mut]
POST   /docker/mos/compose/stacks/{name}/stop - Stop a compose stack [mut]
POST   /docker/mos/compose/stacks/{name}/sync-shas - Sync local SHAs to remote SHAs for a compose stack [mut]
POST   /docker/mos/compose/stacks/{name}/upgrade - Upgrade a compose stack to latest images [mut]
GET    /docker/mos/compose/templates - Get all compose template names
GET    /docker/mos/compose/templates/{name} - Get specific compose template

## Docker WebSocket (2)

GET    /docker/websocket/events - WebSocket Events Documentation
GET    /docker/websocket/stats - Get WebSocket operation statistics

## File Operations WebSocket (1)

GET    /mos/fileoperations/websocket/events - WebSocket Events Documentation

## LLM (2)

POST   /llm/chat - Send a message to the LLM [mut]
GET    /llm/status - Get LLM container status

## LXC (31)

GET    /lxc/backups - List all containers with their backups
GET    /lxc/containers - List all LXC Containers
POST   /lxc/containers/create - Create a new LXC container [mut]
GET    /lxc/containers/usage - Get resource usage for all containers
DELETE /lxc/containers/{name} - Destroy (delete) a container [DEL]
GET    /lxc/containers/{name}/backups - List backups for a specific container
POST   /lxc/containers/{name}/backups - Create a backup of a container [mut]
POST   /lxc/containers/{name}/backups/abort - Abort an active backup operation [mut]
POST   /lxc/containers/{name}/backups/restore - Restore a container from backup [mut]
DELETE /lxc/containers/{name}/backups/{filename} - Delete a specific backup file [DEL]
GET    /lxc/containers/{name}/calc - Calculate container rootfs size
POST   /lxc/containers/{name}/convert-btrfs - Convert container rootfs to BTRFS subvolume [mut]
POST   /lxc/containers/{name}/freeze - Freeze (pause) a container [mut]
POST   /lxc/containers/{name}/kill - Forcefully stop a container (kill) [mut]
GET    /lxc/containers/{name}/mounts - List host bind mounts of a container
POST   /lxc/containers/{name}/mounts - Add host bind mount(s) to a container [mut]
PUT    /lxc/containers/{name}/mounts - Replace all host bind mounts of a container [mut]
DELETE /lxc/containers/{name}/mounts - Remove specific host bind mount(s) from a container [DEL]
POST   /lxc/containers/{name}/restart - Restart a container [mut]
GET    /lxc/containers/{name}/snapshots - List all snapshots for a container
POST   /lxc/containers/{name}/snapshots - Create a snapshot of a container [mut]
DELETE /lxc/containers/{name}/snapshots/{snapshot} - Delete a snapshot [DEL]
POST   /lxc/containers/{name}/snapshots/{snapshot}/clone - Create a new container from a snapshot [mut]
POST   /lxc/containers/{name}/snapshots/{snapshot}/restore - Restore container from a snapshot [mut]
POST   /lxc/containers/{name}/start - Start a container [mut]
POST   /lxc/containers/{name}/stop - Stop a container [mut]
POST   /lxc/containers/{name}/unfreeze - Unfreeze (resume) a container [mut]
GET    /lxc/images - Get available container images/distributions
GET    /lxc/mos/containers - Get container startup order
POST   /lxc/mos/containers - Update container startup order [mut]
GET    /lxc/snapshots - List all containers with their snapshots

## LXC WebSocket (2)

GET    /lxc/websocket/events - WebSocket Events Documentation
GET    /lxc/websocket/stats - Get LXC WebSocket statistics

## MOS (94)

GET    /mos/bootbackupfiles - Get boot backup files
GET    /mos/certificates - Get SSL certificate information
POST   /mos/chmod - Change permissions of a file or folder [mut]
POST   /mos/chown - Change ownership of a file or folder [mut]
POST   /mos/createfile - Create a new file on the filesystem [mut]
POST   /mos/createfolder - Create a new folder on the filesystem [mut]
GET    /mos/dashboard - Get dashboard layout
POST   /mos/dashboard - Update dashboard layout [mut]
GET    /mos/dashboard/interface - Get dashboard network interface setting
POST   /mos/dashboard/interface - Update dashboard network interface setting [mut]
POST   /mos/delete - Delete a file or folder from the filesystem [mut]
GET    /mos/diag - Download diagnostics tar.gz bundle
GET    /mos/download - Download a file from the filesystem
POST   /mos/drivers - Download or upgrade drivers [mut]
DELETE /mos/drivers - Delete a driver [DEL]
POST   /mos/editfile - Edit a file on the filesystem [mut]
GET    /mos/fileoperations - List all file operations
POST   /mos/fileoperations - Start a file copy or move operation [mut]
DELETE /mos/fileoperations/{id} - Cancel a running file operation [DEL]
GET    /mos/fsnavigator - Browse filesystem with directory/file picker
GET    /mos/fsnavigator/bookmarks - List all filesystem bookmarks
POST   /mos/fsnavigator/bookmarks - Replace all filesystem bookmarks [mut]
PUT    /mos/fsnavigator/bookmarks - Create a new filesystem bookmark [mut]
DELETE /mos/fsnavigator/bookmarks - Delete one or all filesystem bookmarks [DEL]
POST   /mos/fsnavigator/calc - Calculate directory size [mut]
GET    /mos/getdrivers - Get available driver releases
GET    /mos/getkernel - Get available kernel releases
GET    /mos/getreleases - Get available MOS releases
GET    /mos/installeddrivers - Get installed drivers
POST   /mos/installtodisk - Install MOS to disk [mut]
GET    /mos/osinfo - Get current MOS and CPU information
GET    /mos/readfile - Read a file from the filesystem
POST   /mos/recreatecerts - Recreate SSL certificates [mut]
POST   /mos/rename - Rename a file or directory [mut]
POST   /mos/restart/service - Restart generic service [mut]
POST   /mos/rollbackkernel - Rollback kernel [mut]
POST   /mos/rollbackos - Rollback MOS [mut]
GET    /mos/runningfsoperations - Get count of running file operations
GET    /mos/sensors - Get mapped sensor values
POST   /mos/sensors - Create sensor mapping(s) [mut]
PUT    /mos/sensors - Replace all sensor mappings [mut]
GET    /mos/sensors/config - Get sensor mapping configuration
GET    /mos/sensors/unmapped - Get unmapped sensors
GET    /mos/sensors/view - Get sensors view settings
POST   /mos/sensors/view - Update sensors view settings [mut]
PATCH  /mos/sensors/{id} - Update an existing sensor mapping [mut]
DELETE /mos/sensors/{id} - Delete a sensor mapping [DEL]
GET    /mos/services - Get all service status
GET    /mos/settings/docker - Get Docker settings
POST   /mos/settings/docker - Update Docker settings [mut]
GET    /mos/settings/lxc - Get LXC settings
POST   /mos/settings/lxc - Update LXC settings [mut]
POST   /mos/settings/network/apply - Confirm pending network changes [mut]
GET    /mos/settings/network/interfaces - Get network interfaces
POST   /mos/settings/network/interfaces - Update network interfaces [mut]
POST   /mos/settings/network/interfaces/reconcile - Reconcile network interfaces [mut]
POST   /mos/settings/network/interfaces/{interfaceName}/vlans - Add VLAN to interface [mut]
DELETE /mos/settings/network/interfaces/{interfaceName}/vlans/{vlanId} - Delete VLAN from interface [DEL]
POST   /mos/settings/network/revert - Revert pending network changes [mut]
GET    /mos/settings/network/services - Get network services
POST   /mos/settings/network/services - Update network services [mut]
GET    /mos/settings/network/services/rsync/config - Get rsync daemon configuration
POST   /mos/settings/network/services/rsync/config - Update rsync daemon configuration [mut]
GET    /mos/settings/network/services/samba/config - Get Samba extra configuration
POST   /mos/settings/network/services/samba/config - Update Samba extra configuration [mut]
GET    /mos/settings/notifications/email - Get email notification provider config
POST   /mos/settings/notifications/email - Update email notification provider config [mut]
GET    /mos/settings/notifications/providers - Get all notification providers
POST   /mos/settings/notifications/providers - Create a new notification provider [mut]
GET    /mos/settings/notifications/providers/{name} - Get a single notification provider
PATCH  /mos/settings/notifications/providers/{name} - Update a notification provider [mut]
DELETE /mos/settings/notifications/providers/{name} - Delete a notification provider [DEL]
GET    /mos/settings/system - Get system settings
POST   /mos/settings/system - Update system settings [mut]
GET    /mos/settings/vm - Get VM settings
POST   /mos/settings/vm - Update VM settings [mut]
GET    /mos/system/network/interfaces - Detect physical network interfaces
GET    /mos/tokens - Get all tokens
POST   /mos/tokens - Update tokens (partial updates supported) [mut]
POST   /mos/update_api - Update the API service [mut]
POST   /mos/update_ui - Update the UI service (nginx) [mut]
POST   /mos/updatekernel - Update kernel [mut]
POST   /mos/updateos - Update MOS [mut]
POST   /mos/upload - Upload a file to the filesystem [mut]
GET    /mos/validatetokens - Validate configured tokens
GET    /mos/zram - Get ZRAM configuration and status
POST   /mos/zram - Update ZRAM configuration [mut]
GET    /mos/zram/algorithms - Get available compression algorithms
POST   /mos/zram/devices - Add a new ZRAM device [mut]
POST   /mos/zram/devices/{id} - Update a ZRAM device [mut]
DELETE /mos/zram/devices/{id} - Delete a ZRAM device [DEL]
GET    /mos/zram/status - Get ZRAM device status
GET    /mos/zswap/algorithms - Get available zswap compression algorithms
GET    /mos/zswap/status - Get swap and zswap status

## MOS Hub (12)

GET    /mos/hub/categories - Get available template categories
POST   /mos/hub/compose/template - Get compose files content [mut]
POST   /mos/hub/docker/template - Get docker template content [mut]
GET    /mos/hub/index - Get template index
GET    /mos/hub/knownrepositories - Get known repository URLs
POST   /mos/hub/plugin/template - Get plugin template content [mut]
GET    /mos/hub/repositories - Get all repository URLs
POST   /mos/hub/repositories - Set repository URLs [mut]
GET    /mos/hub/settings - Get hub settings
POST   /mos/hub/settings - Update hub settings [mut]
GET    /mos/hub/types - Get available template types
POST   /mos/hub/update - Update repositories [mut]

## MOS Plugins (11)

GET    /mos/plugins - List all installed plugins
DELETE /mos/plugins/delete/{pluginName} - Delete a plugin [DEL]
GET    /mos/plugins/driver/{pluginName} - Get driver package info for a driver plugin
POST   /mos/plugins/executefunction - Execute a function from a plugin [mut]
POST   /mos/plugins/install - Install a plugin from Hub template [mut]
POST   /mos/plugins/query - Query a plugin command [mut]
POST   /mos/plugins/releases - Get GitHub releases for a plugin repository [mut]
GET    /mos/plugins/settings/{pluginName} - Get plugin settings
POST   /mos/plugins/settings/{pluginName} - Update plugin settings [mut]
POST   /mos/plugins/update - Update plugins [mut]
POST   /mos/plugins/updatecheck - Check for plugin updates [mut]

## NUT (5)

GET    /nut/scripts/{event} - Get the script for a NUT event
POST   /nut/scripts/{event} - Update the script for a NUT event [mut]
GET    /nut/settings - Get NUT settings
POST   /nut/settings - Update NUT settings [mut]
GET    /nut/status - Get UPS status

## NUT WebSocket (2)

GET    /nut/websocket/events - WebSocket Events Documentation
GET    /nut/websocket/stats - Get NUT WebSocket statistics

## Notifications (10)

GET    /notifications - Get all notifications
DELETE /notifications - Delete all notifications [DEL]
POST   /notifications/push/subscribe - Subscribe to push notifications [mut]
DELETE /notifications/push/subscribe - Unsubscribe from push notifications [DEL]
GET    /notifications/push/vapid-key - Get VAPID public key
PUT    /notifications/read/all - Mark all notifications as read [mut]
PUT    /notifications/read/multiple - Mark multiple notifications as read [mut]
GET    /notifications/stats - Get notification statistics
DELETE /notifications/{id} - Delete notification by ID [DEL]
PUT    /notifications/{id}/read - Mark notification as read [mut]

## Pools (40)

GET    /pools - List all pools
GET    /pools/availablepooltypes - Get available pool types
POST   /pools/bcachefs - Create bcachefs pool [mut]
POST   /pools/mergerfs - Create MergerFS pool [mut]
POST   /pools/multi - Create multi-device BTRFS pool [mut]
POST   /pools/nonraid - Create NonRAID pool [mut]
POST   /pools/nonraid/adddevice - Add data device to NonRAID pool [mut]
POST   /pools/nonraid/addparity - Add parity device to NonRAID pool [mut]
POST   /pools/nonraid/replace - Replace devices in a NonRAID pool [mut]
PUT    /pools/order - Update order of all pools [mut]
POST   /pools/single - Create single device pool [mut]
GET    /pools/vpools - List all vpools (MergerFS Path Pools)
POST   /pools/vpools - Create a vpool (MergerFS Path Pool) [mut]
PUT    /pools/vpools/order - Update vpool display order [mut]
GET    /pools/vpools/{id} - Get a vpool by ID
DELETE /pools/vpools/{id} - Delete a vpool by ID [DEL]
POST   /pools/vpools/{id}/automount - Toggle automount for a vpool [mut]
POST   /pools/vpools/{id}/mount - Mount a vpool by ID [mut]
POST   /pools/vpools/{id}/unmount - Unmount a vpool by ID [mut]
GET    /pools/{id} - Get pool by ID
DELETE /pools/{id} - Remove pool by ID [DEL]
POST   /pools/{id}/automount - Toggle automount setting for a pool [mut]
POST   /pools/{id}/bcachefs/scrub - Execute bcachefs scrub operation [mut]
POST   /pools/{id}/btrfs/balance - Execute BTRFS balance operation [mut]
POST   /pools/{id}/btrfs/scrub - Execute BTRFS scrub operation [mut]
PATCH  /pools/{id}/comment - Update pool comment [mut]
GET    /pools/{id}/config - Get pool configuration
PATCH  /pools/{id}/config - Update pool configuration [mut]
POST   /pools/{id}/devices - Add devices to pool [mut]
POST   /pools/{id}/devices/add - Add devices to an existing pool [mut]
POST   /pools/{id}/devices/remove - Remove devices from an existing pool [mut]
POST   /pools/{id}/devices/replace - Replace a device in a pool [mut]
POST   /pools/{id}/mount - Mount pool by ID [mut]
POST   /pools/{id}/parity - Execute parity operation on a MergerFS or NonRAID pool [mut]
POST   /pools/{id}/parity/add - Add parity devices to a MergerFS pool [mut]
POST   /pools/{id}/parity/remove - Remove parity devices from a MergerFS pool [mut]
POST   /pools/{id}/parity/replace - Replace a parity device in a MergerFS pool [mut]
POST   /pools/{id}/shared - Toggle shared mount propagation for a pool [mut]
GET    /pools/{id}/status - Get pool status
POST   /pools/{id}/unmount - Unmount pool by ID [mut]

## Pools WebSocket (2)

GET    /pools/websocket/events - WebSocket Events Documentation
GET    /pools/websocket/stats - Get WebSocket monitoring statistics

## Remotes (10)

GET    /remotes - List all remote shares
POST   /remotes - Create new remote share [mut]
POST   /remotes/connectiontest - Test connection to remote share without saving [mut]
POST   /remotes/listshares - List all available shares from a server [mut]
GET    /remotes/{id} - Get remote share by ID
PUT    /remotes/{id} - Update remote share [mut]
DELETE /remotes/{id} - Delete remote share [DEL]
POST   /remotes/{id}/mount - Mount remote share [mut]
GET    /remotes/{id}/status - Get remote share mount status
POST   /remotes/{id}/unmount - Unmount remote share [mut]

## SMART (10)

GET    /disks/smart/config - Get SMART monitoring configuration
PUT    /disks/smart/config - Update global SMART configuration [mut]
GET    /disks/smart/config/disks/{device} - Get SMART config for a specific disk
PUT    /disks/smart/config/disks/{device} - Update SMART config for a specific disk [mut]
DELETE /disks/smart/config/disks/{device} - Delete disk SMART config [DEL]
POST   /disks/smart/config/disks/{device}/acknowledge - Acknowledge current SMART errors for a disk [mut]
DELETE /disks/smart/config/disks/{device}/acknowledge - Clear acknowledged SMART errors for a disk [DEL]
GET    /disks/smart/config/orphaned - List orphaned disk entries
DELETE /disks/smart/config/orphaned - Delete all orphaned entries [DEL]
DELETE /disks/smart/config/orphaned/{serial} - Delete a specific orphaned entry [DEL]

## Shares (19)

GET    /shares - Get all shares configuration
GET    /shares/info - Get shares information/statistics
GET    /shares/nfs - Get NFS shares only
POST   /shares/nfs - Create new NFS share [mut]
GET    /shares/nfs/{shareId} - Get a specific NFS share
PUT    /shares/nfs/{shareId} - Update a NFS share [mut]
DELETE /shares/nfs/{shareId} - Delete a NFS share [DEL]
GET    /shares/nfs/{shareId}/target-devices - Get target devices for a specific NFS share
PUT    /shares/nfs/{shareId}/target-devices - Update target devices for a NFS share [mut]
DELETE /shares/nfs/{shareId}/target-devices - Remove target devices from a NFS share [DEL]
GET    /shares/pools - Get available pools for share creation
GET    /shares/smb - Get SMB shares only
POST   /shares/smb - Create new SMB share [mut]
GET    /shares/smb/{shareId} - Get a specific SMB share
PUT    /shares/smb/{shareId} - Update a SMB share [mut]
DELETE /shares/smb/{shareId} - Delete a SMB share [DEL]
GET    /shares/smb/{shareId}/target-devices - Get target devices for a specific share
PUT    /shares/smb/{shareId}/target-devices - Update target devices for a share [mut]
DELETE /shares/smb/{shareId}/target-devices - Remove target devices from a share [DEL]

## System (18)

GET    /system/detailed - Get detailed system information
GET    /system/devices/pci - Get PCI devices information
GET    /system/devices/usb - Get USB devices information
GET    /system/governors - Get available CPU governors
GET    /system/gpus - Get GPU information
GET    /system/keymaps - List available keymaps
GET    /system/load - Get system load, temperature, memory and network utilization
GET    /system/logs - List all log files
GET    /system/logs/content - Read log file content
GET    /system/memory - Get detailed memory information
POST   /system/power/reboot - Reboot system [mut]
POST   /system/power/shutdown - Shutdown system [mut]
GET    /system/proxy - Get proxy settings
PUT    /system/proxy - Update proxy settings [mut]
GET    /system/sensors - Get hardware sensor data
GET    /system/timedate - Get current system date and time
PUT    /system/timedate - Set system date and/or time [mut]
GET    /system/timezones - List available timezones

## System Load WebSocket (2)

GET    /system/websocket/events - WebSocket Events Documentation
GET    /system/websocket/stats - Get WebSocket monitoring statistics

## Terminal (5)

POST   /terminal/create - Create new terminal session [mut]
GET    /terminal/sessions - List all terminal sessions
GET    /terminal/{sessionId} - Terminal session info
DELETE /terminal/{sessionId} - Terminate terminal session [DEL]
POST   /terminal/{sessionId}/resize - Resize terminal [mut]

## Terminal WebSocket (2)

GET    /api/v1/terminal/websocket/events - Terminal WebSocket Events Documentation
GET    /api/v1/terminal/websocket/stats - Get Terminal WebSocket Statistics

## Users (7)

GET    /users - Get users (admin sees all, user sees only themselves)
GET    /users/me - Get own user profile
PUT    /users/me - Update own user profile [mut]
PUT    /users/root - Change root password [mut]
GET    /users/{id} - Get specific user (admin only)
PUT    /users/{id} - Update user (admin only for other users) [mut]
DELETE /users/{id} - Delete user (admin only) [DEL]

## VM (28)

GET    /vm/binfmt_architectures - Get available binfmt architectures
GET    /vm/capabilities - Get VM capabilities
GET    /vm/index - Get VM index
PUT    /vm/index - Update VM index [mut]
GET    /vm/machines - List all virtual machines
POST   /vm/machines - Create a new virtual machine [mut]
GET    /vm/machines/usage - Get resource usage for all VMs
DELETE /vm/machines/{name} - Delete a virtual machine [DEL]
GET    /vm/machines/{name}/autostart - Get autostart status of a virtual machine
PUT    /vm/machines/{name}/autostart - Set autostart status for a virtual machine [mut]
GET    /vm/machines/{name}/calc - Calculate VM disk sizes
GET    /vm/machines/{name}/config - Get simplified VM configuration
PUT    /vm/machines/{name}/config - Update VM with simplified configuration [mut]
POST   /vm/machines/{name}/kill - Kill a virtual machine (force stop) [mut]
POST   /vm/machines/{name}/reset - Reset a virtual machine (hard reset) [mut]
POST   /vm/machines/{name}/restart - Restart a virtual machine (graceful reboot) [mut]
POST   /vm/machines/{name}/start - Start a virtual machine [mut]
POST   /vm/machines/{name}/stop - Stop a virtual machine (graceful shutdown) [mut]
GET    /vm/machines/{name}/xml - Get raw VM XML
PUT    /vm/machines/{name}/xml - Update VM XML directly [mut]
GET    /vm/machinetypes - Get available QEMU machine types
POST   /vm/virtioiso/cleanup - Cleanup old VirtIO ISOs [mut]
POST   /vm/virtioiso/download - Download a VirtIO ISO [mut]
GET    /vm/virtioiso/installed - Get installed VirtIO ISOs
GET    /vm/virtioiso/versions - Get available VirtIO ISO versions
GET    /vm/vnc/sessions - Get active VNC sessions
POST   /vm/vnc/token - Generate VNC access token [mut]
POST   /vm/xml/validate - Validate VM XML [mut]

## VM WebSocket (2)

GET    /vm/websocket/events - WebSocket Events Documentation
GET    /vm/websocket/stats - Get VM WebSocket statistics

## iSCSI Initiators (9)

GET    /iscsi/initiator - Get iSCSI initiator configuration
PUT    /iscsi/initiator/name - Update initiator name [mut]
POST   /iscsi/initiator/targets - Add a new target [mut]
GET    /iscsi/initiator/targets/{targetId} - Get a specific target
PUT    /iscsi/initiator/targets/{targetId} - Update a target [mut]
DELETE /iscsi/initiator/targets/{targetId} - Remove a target [DEL]
POST   /iscsi/initiator/targets/{targetId}/login - Login to a target [mut]
POST   /iscsi/initiator/targets/{targetId}/logout - Logout from a target [mut]
POST   /iscsi/initiator/test-connection - Test connection to a target [mut]

## iSCSI Targets (10)

GET    /iscsi/targets - Get all iSCSI targets
POST   /iscsi/targets - Create new iSCSI target [mut]
GET    /iscsi/targets/info - Get iSCSI targets statistics
POST   /iscsi/targets/restart - Restart all iSCSI targets [mut]
GET    /iscsi/targets/{targetId} - Get a specific iSCSI target
PUT    /iscsi/targets/{targetId} - Update an iSCSI target [mut]
DELETE /iscsi/targets/{targetId} - Delete an iSCSI target [DEL]
POST   /iscsi/targets/{targetId}/luns - Add a LUN to an iSCSI target [mut]
PUT    /iscsi/targets/{targetId}/luns/{lunId} - Update a LUN in an iSCSI target [mut]
DELETE /iscsi/targets/{targetId}/luns/{lunId} - Remove a LUN from an iSCSI target [DEL]
