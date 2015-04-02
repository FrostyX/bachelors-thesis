SELECT DISTINCT pkgtups.name
FROM trans_beg JOIN trans_data_pkgs JOIN pkgtups
ON trans_data_pkgs.pkgtupid=pkgtups.pkgtupid
AND trans_data_pkgs.tid=trans_beg.tid
WHERE  trans_beg.timestamp > t
