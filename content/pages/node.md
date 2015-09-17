Title: Node JS repo
lang: en

    :::text
    [nodesource]
    name=Node.js Packages for Enterprise Linux 7 - $basearch
    baseurl=https://rpm.nodesource.com/pub/el/7/$basearch
    failovermethod=priority
    enabled=1
    gpgcheck=1
    gpgkey=file:///etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL
    
    [nodesource-source]
    name=Node.js for Enterprise Linux 7 - $basearch - Source
    baseurl=https://rpm.nodesource.com/pub/el/7/SRPMS
    failovermethod=priority
    enabled=0
    gpgkey=file:///etc/pki/rpm-gpg/NODESOURCE-GPG-SIGNING-KEY-EL
    gpgcheck=1
