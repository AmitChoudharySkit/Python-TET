#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Error: No directory path provided."
    echo "Usage: $0 <directory_path>"
    exit 1
fi


SOURCE_DIR="$1"
BACKUP_DIR="$HOME/backups"
DATE=$(date +"%Y-%m-%d_%H-%M")
BACKUP_FILE="backup_$DATE.tar.gz"
LOG_FILE="$BACKUP_DIR/backup.log"


mkdir -p "$BACKUP_DIR"


log_message() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") - $1" >> "$LOG_FILE"
}


if [ ! -d "$SOURCE_DIR" ]; then
    log_message "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi


log_message "Starting backup of '$SOURCE_DIR'"
if tar -czf "$BACKUP_DIR/$BACKUP_FILE" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"; then
    log_message "Backup completed successfully: $BACKUP_FILE"
    echo "Backup completed successfully: $BACKUP_FILE"
else
    log_message "Error: Backup failed"
    echo "Error: Backup failed. Check $LOG_FILE for details."
    exit 1
fi


BACKUP_SIZE=$(du -h "$BACKUP_DIR/$BACKUP_FILE" | cut -f1)
log_message "Backup file size: $BACKUP_SIZE"
echo "Backup file size: $BACKUP_SIZE"

exit 0