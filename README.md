# Python Network Connectivity Mini Lab

I wanted to put a bit of Python into practice using the Windows home lab I'd already built. For this mini lab, I wrote a small script to check whether I could reach my Hyper-V domain controller on TCP port 53.

## What the script does

I kept the first version simple. `lab_monitor.py` uses Python's built-in `socket` module to try connecting to **DC01 (`10.10.10.10`) on TCP port 53**, with a three-second timeout. It checks the result from `connect_ex()`, prints **SUCCESS** or **FAILED**, then closes the socket.

## Writing the script

This is the script in VS Code while I was putting it together on **21 November 2026**. It shows the target address, timeout and `if`/`else` check. The terminal at this stage shows an earlier run that printed the starting message; the completed connectivity tests are below.

![Python connectivity script being written in VS Code](<screenshots/Screenshot 2026-11-21 195108.png>)

## What I tested

I ran the script from my Windows host against my Windows Server 2025 VM. With DC01 switched off, the check failed. After I started the VM, I ran it again and got a successful connection:

| Test | Observed result |
|---|---|
| DC01 was offline | `FAILED: DC01 DNS TCP port 53 is not reachable.` |
| DC01 was started | `SUCCESS: DC01 DNS TCP port 53 is reachable!` |

Seeing both results helped me connect what the code was doing with what was happening in my lab. This screenshot shows both runs from **21 November 2026**.

![Python terminal showing failed and successful TCP connectivity checks](screenshots/01-python-connectivity-test.png)

## Running the Script

I ran the Python script on my Windows 11 PC using VS Code, connecting to my Windows Server 2025 virtual machine through Hyper-V.

To run the script, I used:

```powershell
python lab_monitor.py
```

The script attempted a TCP connection to DC01 on port 53 and displayed whether the connection succeeded or failed.

## What I learned

- Importing and using Python's standard library.
- Storing a target address in a variable.
- Creating a socket and setting a timeout.
- Using an `if`/`else` statement to report a connection result.
- Comparing failed and successful checks while troubleshooting VM availability.

The script runs one TCP connectivity check each time I start it. A successful result tells me TCP port 53 is reachable; checking DNS name resolution or UDP DNS traffic would need a separate test. In this lab, starting DC01 restored connectivity.

**Mini lab complete — 21 November 2026.** A small first step into Python automation, built and tested against my own home lab. The script here is the original version I used.
