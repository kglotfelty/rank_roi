



for meth in max min big small bright faint
do
  /bin/rm -rf $meth
  mkdir $meth
  rank_roi sim.img roi="roi_?.reg" out="$meth/rank_{}.reg" meth=$meth clob+

  mkregmap sim.img "$meth/rank_?.reg" out=$meth.map clob+

done
