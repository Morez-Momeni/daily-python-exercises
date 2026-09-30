# Problem 64: Extract Process Name and ID from System Logs

## Problem
Parse system log lines and extract the **process name** and **process ID** from entries that contain the pattern `name[pid]:`.

The regex was tested against real system logs and matches lines in this shape:
2026-09-30T14:22:02.234567+00:00 myhost sshd[1234]: Accepted password ...


## My Regex Pattern

```regex
^(?:[0-9\-\:\.\+T]+)\s(?:[a-zA-Z0-9_\-]+)\s(?P<PsName>[a-zA-z\-.]+)\[(?P<PsId>[0-9]+)\]
```