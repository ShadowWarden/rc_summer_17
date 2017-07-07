<?php
/* howto.php
*  Omkar H. Ramachandran
*  omkar.ramachandran@colorado.edu
*
*  Only works if you have 1 saved figure. Fixes the php file given in the HOWTO page
*  in the XDMoD website.
*/


$data = 'a:2:{s:14:"query_metadata";a:2:{s:5:"maxid";i:0;s:4:"data";a:1:{i:0;a:2:{s:16:"queries_migrated";b:1;s:8:"recordid";i:0;}}}s:13:"queries_store";a:2:{s:5:"maxid";i:4;s:4:"data";a:1:{i:4;a:4:{s:4:"name";s:12:"summit_chart";s:6:"config";s:1454:"{"featured":false,"trend_line":false,"x_axis":{},"y_axis":{},"legend":{},"defaultDatasetConfig":{},"swap_xy":false,"share_y_axis":false,"hide_tooltip":false,"show_remainder":false,"timeseries":true,"title":"Total CPU Hours Summary : OHR","legend_type":"right_center","font_size":3,"show_filters":false,"show_warnings":false,"data_series":{"data":[{"id":1e-14,"metric":"total_cpu_hours","category":"","realm":"Jobs","group_by":"resource","x_axis":false,"log_scale":false,"has_std_err":false,"std_err":false,"std_err_labels":"","value_labels":false,"display_type":"column","line_type":"","line_width":"","combine_type":"stack","sort_type":"value_desc","filters":{"data":[],"total":0},"ignore_global":false,"long_legend":true,"trend_line":"","color":"","shadow":"","visibility":"","z_index":null,"enabled":false},{"group_by":"none","color":"auto","log_scale":false,"std_err":false,"value_labels":false,"display_type":"line","combine_type":"side","sort_type":"value_desc","ignore_global":false,"long_legend":true,"x_axis":false,"has_std_err":false,"trend_line":false,"line_type":"Solid","line_width":2,"shadow":false,"filters":{"data":[],"total":0},"z_index":1,"visibility":null,"enabled":true,"metric":"avg_cpu_hours","realm":"Jobs","category":"Jobs","id":0.7019138689092076}],"total":2},"aggregation_unit":"Auto","global_filters":{"data":[],"total":0},"timeframe_label":"User Defined","start_date":"2017-06-01","end_date":"2017-06-30","start":0,"limit":10}";s:2:"ts";d:1499461037.9460001;s:8:"recordid";i:4;}}}}'; // Copy your data into this variable.
$profile = unserialize($data);
echo "Copy and paste the following in the Summary Charts section of roles.json\n\n";
print_r($profile['queries_store']['data']['4']['config']);
echo "\n";
?>
