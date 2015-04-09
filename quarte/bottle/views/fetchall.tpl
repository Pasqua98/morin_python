<h1>Risultato della query: showall</h1>

<ul>
    % for row in rows:
    <li>
       % for e in row: 
       {{e}} 
       % end
    </li>
    % end
</ul>        



