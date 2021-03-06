<h1> 21_diceware </h1>

<p>Generating secure and memorable passwords for bitcoin </p>

<h3> Example </h3>
<p>This service generates secure, memorable passwords for your apps or services, in exchange for bitcoin. </p>
<p> To purchase a diceware password run: </p>

<pre><code>21 buy 'http://[fcce:a977:ee7d:817b:3380:0000:0000:0001]:8000/make_password'
</code></pre>

<p>Then you will receive a json string of 5 (default) random generated words, in the form of a dictionary.</p>
<pre><code> {
    "password": [
        "alps",
        "push",
        "craft",
        "assam",
        "mc"
    ]
}
</code></pre>

<p> To spesify a password length, add the desirable number of words as an integer at the end of the url, for example: </p>

<pre><code>
21 buy 'http://[fcce:a977:ee7d:817b:3380:0000:0000:0001]:8000/make_password/11'
</code></pre>

<p> Maximum password length allowed is 16 words. </p>

<h3> Requirements </h3>

1. A  <a href="https://21.co">21 Bitcoin Computer</a> or 21 installed on AWS or MacOS
2. You need to be connected to the 21 Network

