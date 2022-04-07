from scapy.all import DNS, DNSQR, IP, sr1, UDP

dns_request = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=input('Enter website: ')))

answer = sr1(dns_request, verbose=0)

print(answer[DNS].summary())

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
# Your branch is up to date with 'origin/main'.
#
# Changes to be committed:
#	new file:   test.txt
#
