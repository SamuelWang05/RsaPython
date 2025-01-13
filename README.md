# RsaFPGA
Implementation of a RSA encryption algorithm on an FPGA.

# What is RSA?
RSA was developed in 1977 by three cryptographers: Ron Rivest, Adi Shamir, and Leonard Adleman (the name RSA comes from the combination of their last names). To give a very brief overview of RSA: each person has a public and private key - the public key can be seen by anyone, while the private key should secret. When Alice is sending a message to Bob, she encrypts the message using Bob's public key. Once Bob receives the encrypted message, he can decrypt it with his own private key. If anyone intercepts the encrypted message, it is nearly impossible to brute force the private key to decrypt the message. The actual math to generate the keys is shown below.

# Math to Generate Keys
The following steps are used to generate the public and private keys:
_Currently in progress_

# Development Phase 1 - Learning RSA
Before developing anything on an FPGA, I first spent time studying RSA and understanding the math behind it. Then, to solidify my understanding, I developed a rudimentary Python program to implement the RSA algorithm.
