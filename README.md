# Introduction
Street Fight is a fighting game between 2 players, each of them have one single mission: defeat their opponent. Street Fight developed using Python and Pygame library.

# How to install
* Step 1: [Click here to download the game.](https://github.com/ConKienHuy/Street-Fight/archive/refs/heads/master.zip)
* Step 2: In your machine, open your terminal (or in Windows is `cmd`).
* Step 3: Type `pip install pygame`.
    * Please note that many Linux distro like Ubuntu, Kali Linux... have pygame preinstalled. So in our case (using Kali Linux), calling `pip install pygame` will result this:
<p align="center">
    <img src="https://lh3.googleusercontent.com/pw/AP1GczOEesqmJPdiapJE3oPZkGn7dKAaUtC-NMex_QonH5NsVhapB4wkpsrNifVU96otrGvCVm4SnBcL-LSRNZBv7tq4jlKB_ESJPZihGa9hIkfmOAoZDGBjm9YYjVR9ot3Qmgli8H60WTmiVOE6DW4UX64T=w739-h194-s-no-gm" alt="terminal" width="600px">
</p>

* Step 4: Move to your game directory using `cd`.
* Step 5: Choose a machine that will become your server, and check its IP address.
    * In Windows, type `ipconfig`, and find your IPv4 in ethernet (if you're connected via ethernet), or wifi...
   <p align="center">
       <img src="https://lh3.googleusercontent.com/pw/AP1GczNVfH0MMEtJUlIRXp_EBTLWJCHdWqwXTNJmFrKj9dT5A9J8M2bvhTWCHmNqktyOvsby_25jQW1fFHyIuk7vJ-j4xdoFeDS6m7sWg2oR2kr15SZblIb97S0M5vpynme8agNfp9VZerVnxqAikI9vjBIS=w745-h628-s-no-gm" alt="win_ip">
   </p>
   
    * In Linux, type `hostname -i`.
   <p align="center">
       <img src="https://lh3.googleusercontent.com/pw/AP1GczM-FR21taPM74FsWm7xlfDOcaQ_NmiElzaKyqFIgBRGewrpfBXrCYG2zkOqoFKkIw8dojnrt5Rtbvkerd7H6CNnvUMn4tUtgfKMNwxuSSbWaKuXXMGCKmc_t3wM5F526r7TJtDKpCfx3ZbcYTzOGeOK=w299-h128-s-no-gm" alt="linux_ip">
   </p>

* Step 6: In your server PC, paste the IP in `server.py`. In your client PCs, paste it in `main.py`.
<p align="center">
    <img src="https://lh3.googleusercontent.com/pw/AP1GczOac8_b_tdztdYlFvK30ORuSUwwPu5PO4QbluiIkJ-A9e6trTpFmGoVRs8D0U6hCGtkB42yFbmvzJ-K4QBcTj5rGHZVYG2akG2Bpie_PZi1GgkFaZzuCFGyosDo3EeB3Et726MxAcn4xyrmfAHUu-zj=w1240-h454-s-no-gm" alt="fix_ip">
</p>
    
* Step 7: Type `py server.py` or `python3 server.py` to launch server.
    *  Please note that depend on your operating system, one of them work, and the other doesn't.
    *  In our test cases, `py server.py` works in Windows 11. And in Kali Linux, the command is `python3 server.py`.
* Step 8: Type `py main.py` or `python3 main.py` to launch the game.
* Step 9: Repeat step 8 in the second computer.

# Game footage
<p align="center">
    <img src="https://lh3.googleusercontent.com/pw/AP1GczNEeiJcJjI8UjTsMSwpVKJ6IV0flLyj9hKaxGVbZpUNnvX_8X2EOc5CaWeKnn7Wi2O6wJdS_1e0AZY4oUTn0HJxkW0nqtZ7HUOFSjy7Jq041xHi_lia6Qnj_kbkBckY4lNLdFh5SEeOEM6LHImq2JSs=w1545-h869-s-no-gm" alt="main_menu">
</p>
<p align="center">
    <img src="https://lh3.googleusercontent.com/pw/AP1GczNyFq9Mz4E1sTKRkAXPblIYzyGlXrOA6J6ZkyHe_gAQpPEowfO4Ump3wgC4MKKbkeg0ChxgXB81QvwoHkrqHfF_HFkmnq2AR_iMAcc0aWDw1czuGANncPOqwbj6Z-OYi1ZqnBbms5ytjfuDurfKj0e3=w1300-h731-s-no-gm" alt="chat">
</p>
<p align="center">
    <img src="https://lh3.googleusercontent.com/pw/AP1GczM0_ln5vadf5CVC_GKyWBqSGpczLO2lBaMNqak88MxbhdnlVuVc5OvHns0q71L4YX64ouP3upPYfies9UaPkAzmjjVnH74Cpr0KXn6JvNeO9pHQ4b7GqFvfwGC5F_93P6tU0GhUKYmpMHKYStIQ7KBa=w1300-h731-s-no-gm" alt="fight">
</p>

# Developers
* [Con Kien Huy](https://github.com/ConKienHuy)
* [Tran Tuan Sang](https://ttsang793.github.io)
* [Nguyen Hoang Tuan](https://github.com/tuansgu)