# 21_diceware
<p>Generating secure and memorable passwords for bitcoin <p>

<h3> Example </h3>
<p>This service generates secure, memorable password suggestions for your apps or services, in exchange for bitcoin. </p>
<p> To purchase a diceware password run: </p>

<pre><code>21 buy url http://10.244.192.155:5000/make_password
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
21 buy url http://10.244.192.155:5000/make_password/11 
</code></pre>

<p> Maximum password length allowed is 16 words. </p>

<h3> Requirements </h3>

<ul>
<li>Having a  <a href="https://21.co">21 Bitcoin Computer</a> or 21 running on AWS or MacOS <li> </ul>
<li>Be connected to the 21 Network</li> 
<li><Having the 21 library and its dependencies installed</li>
</ul>
