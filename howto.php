<?php
/* howto.php
*  Omkar H. Ramachandran
*  omkar.ramachandran@colorado.edu
*
*  Only works if you have 1 saved figure. Fixes the php file given in the HOWTO page
*  in the XDMoD website.
*/


$data = ''; // Copy your data into this variable.
$profile = unserialize($data);
echo "Copy and paste the following in the Summary Charts section of roles.json\n\n";
print_r($profile['queries_store']['data']['4']['config']);
echo "\n";
?>
