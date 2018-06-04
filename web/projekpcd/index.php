<?php
    // $command = escapeshellcmd('/test.py');
    // $output = shell_exec($command);
    $result = exec("py -3 web.py C:/xampp/htdocs/projekpcd");
    echo $result;
?>