URL: index.html
save_as: gpg/index.html
Title: GPG key
Hide: True
Template: openpgp

If you want to send me a mail, you can use my public GPG key: [5AA32256](http://roidelapluie.be/gpg/5AA32256.pub).

My preferred email address is [roidelapluie@inuits.eu](mailto:roidelapluie@inuits.eu).

    ::
    pub   1024D/5AA32256 2010-01-14
          Key fingerprint = 19E6 703D 4113 236A 4C1F  B492 9ADD 8741 5AA3 2256
    uid                  Julien Pivotto (roidelapluie) <roidelapluie@inuits.eu>
    uid                  Julien Pivotto (roidelapluie) <roidelapluie@roidelapluie.be>
    uid                  Julien Pivotto <julien@inuits.eu>
    uid                  Julien Pivotto <julien.pivotto@gmail.com>
    uid                  Julien Pivotto (roidelapluie) <roidelapluie@gmail.com>
    uid                  [jpeg image of size 5136]
    uid                  Julien Pivotto (roidelapluie) <roidelapluie@esquimaux.be>
    uid                  Julien Pivotto <julien@esquimaux.be>
    uid                  Julien Pivotto <julien.pivotto@alcatel-lucent.com>
    sub   8192R/341A726C 2013-02-05
    sub   8192R/66748C55 2013-02-05


# Tell me something private

You want to send me an encrypted mail? Better than nothing, you can encrypt your mail body here, thanks to [OpenPGP.js](http://openpgpjs.org/).

Please note that this is less secure that using opengpg. Please also note that the
data will just be encrypted, not signed.

Please send the mail as plain text (not in HTML).

### Input

<textarea class="opengpginput">Your text here.</textarea>
<div style="text-align:center;"><a href="#pgpoutput" class="opengpgbutton">Encrypt</a></div>

### Output

<pre id="pgpoutput" class="opengpgoutput">Encrypted text will be in this box.</pre>

Note: You have to copy-paste the content of the box in a new mail. It is not sent automatically.
