#!/usr/bin/env python3

db = {'astronomy': '''Pulsars, 
        Supermassive black holes,
        Kepler telescope, 
        Light level drops when planet transits.
    ''',
    
    'decadent_society': '''    <h1>The Decadent Society</h1>
    <h2>Ross Douthat</h2>
    <ul>
      <li>Economic Stagnation</li>
      <li>Infertility</li>
      <li>Sclerosis</li>
      <li>Cultural Repetition</li>
      <li>Renaissance</li>
    </ul>

    <p>Fat, Stoned and Distracted</p>
''',
'markdown':"""    <h1>Markdown</h1>

    <table class="pure-table">
      <thead>
        <tr>
          <th>Item</th>
          <th>How</th>
        </tr>
      </thead>
      <tr>
        <td>Code</td>
        <td>Surround in backticks</td>
      </tr>
    </table>
    <a href="https://daringfireball.net/projects/markdown">docs</a>
""",
'useful_packages':
"""    <h1>Useful packages and tools</h1>
    <table class="pure-table">
      <thead>
      <tr>
        <th>Name</th>
        <th>Link</th>
      </tr>
      <tr>
        </thead>
        <tbody>
        <td>http-server</td>
        <td>
          <a href="https://www.npmjs.com/package/http-server">http-server</a>
        </td>
      </tr>
      <tr>
        <td>Pure CSS</td>
        <td><a href="https://purecss.io/">Link</a></td>
      </tr>
      </tbody>
    </table>
"""}

def export_data(data):
  import pickle

  with open('data/db.pkl', 'wb') as f:
      pickle.dump(data,f)

if __name__=='__main__':
  export_data(db)