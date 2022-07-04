#!/bin/bash

runfile_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run115_220701102319.raw"
runfile_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run115_220701102319.raw"

#do not touch here
if [ 1 -eq 1 ]; then
echo "Analysis..."
	corry -c analysis.conf -o detectors_file="geometries/geoid6_dut_aligned.geo" -o histogram_file="analysis.root" -o EventLoaderEUDAQ2.file_name=$runfile_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_dut
fi

exit 0
