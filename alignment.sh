#!/bin/bash

#choose which geoid to align
align_geoid1=0	#not tested
align_geoid2=0	#good
align_geoid3=0	#not tested
align_geoid4=0	#good
align_geoid5=0	#not tested
align_geoid6=0	#currently tested
align_geoid7=0	#not tested
align_geoid8=0	#not tested
align_geoid9=1	#not tested


#Choose runfiles for alignment per geoid
runfile_geoid1_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run4673_220627231559.raw"
runfile_geoid2_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run4675_220628120228.raw"
runfile_geoid3_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run4696_220628220619.raw"
runfile_geoid4_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run071_220629234406.raw"
runfile_geoid5_tele=
runfile_geoid6_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run087_220630132510.raw"
runfile_geoid7_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run175_220701134804.raw"
runfile_geoid8_tele=
runfile_geoid9_tele="/home/testbeam1/data/data_producer_runs/desy/telescope_run240_220702102138.raw"

runfile_geoid1_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run4673_220627231559.raw"
runfile_geoid2_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run4675_220628120228.raw"
runfile_geoid3_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run4696_220628220619.raw"
runfile_geoid4_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run071_220629234406.raw"
runfile_geoid5_dut=
runfile_geoid6_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run087_220630132510.raw"
runfile_geoid7_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run175_220701134804.raw"
runfile_geoid8_dut=
runfile_geoid9_dut="/home/testbeam1/data/data_producer_runs/desy/mpx2_run240_220702102219.raw"

#do not touch here
if [ $align_geoid1 -eq 1 ]; then
echo "Aligning geoID 1..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid1.geo" -o detectors_file_updated="geometries/geoid1_tel_prealigned.geo" -o histogram_file="geoid1_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid1_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid1_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid1_tel_aligned.geo" -o histogram_file="geoid1_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid1_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid1_tel_aligned.geo" -o detectors_file_updated="geometries/geoid1_dut_prealigned.geo" -o histogram_file="geoid1_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid1_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid1_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid1_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid1_dut_aligned.geo" -o histogram_file="geoid1_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid1_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid1_dut
fi

if [ $align_geoid2 -eq 1 ]; then
echo "Aligning geoID 2..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid2.geo" -o detectors_file_updated="geometries/geoid2_tel_prealigned.geo" -o histogram_file="geoid2_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid2_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid2_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid2_tel_aligned.geo" -o histogram_file="geoid2_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid2_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid2_tel_aligned.geo" -o detectors_file_updated="geometries/geoid2_dut_prealigned.geo" -o histogram_file="geoid2_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid2_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid2_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid2_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid2_dut_aligned.geo" -o histogram_file="geoid2_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid2_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid2_dut
fi

if [ $align_geoid3 -eq 1 ]; then
echo "Aligning geoID 3..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid3.geo" -o detectors_file_updated="geometries/geoid3_tel_prealigned.geo" -o histogram_file="geoid3_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid3_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid3_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid3_tel_aligned.geo" -o histogram_file="geoid3_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid3_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid3_tel_aligned.geo" -o detectors_file_updated="geometries/geoid3_dut_prealigned.geo" -o histogram_file="geoid3_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid3_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid3_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid3_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid3_dut_aligned.geo" -o histogram_file="geoid3_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid3_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid3_dut
fi

if [ $align_geoid4 -eq 1 ]; then
echo "Aligning geoID 4..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid4.geo" -o detectors_file_updated="geometries/geoid4_tel_prealigned.geo" -o histogram_file="geoid4_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid4_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid4_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid4_tel_aligned.geo" -o histogram_file="geoid4_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid4_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid4_tel_aligned.geo" -o detectors_file_updated="geometries/geoid4_dut_prealigned.geo" -o histogram_file="geoid4_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid4_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid4_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid4_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid4_dut_aligned.geo" -o histogram_file="geoid4_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid4_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid4_dut
fi

if [ $align_geoid5 -eq 1 ]; then
echo "Aligning geoID 5..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid5.geo" -o detectors_file_updated="geometries/geoid5_tel_prealigned.geo" -o histogram_file="geoid5_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid5_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid5_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid5_tel_aligned.geo" -o histogram_file="geoid5_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid5_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid5_tel_aligned.geo" -o detectors_file_updated="geometries/geoid5_dut_prealigned.geo" -o histogram_file="geoid5_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid5_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid5_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid5_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid5_dut_aligned.geo" -o histogram_file="geoid5_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid5_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid5_dut
fi

if [ $align_geoid6 -eq 1 ]; then
echo "Aligning geoID 6..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid6.geo" -o detectors_file_updated="geometries/geoid6_tel_prealigned.geo" -o histogram_file="geoid6_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid6_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid6_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid6_tel_aligned.geo" -o histogram_file="geoid6_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid6_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid6_tel_aligned.geo" -o detectors_file_updated="geometries/geoid6_dut_prealigned.geo" -o histogram_file="geoid6_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid6_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid6_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid6_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid6_dut_aligned.geo" -o histogram_file="geoid6_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid6_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid6_dut
fi

if [ $align_geoid7 -eq 1 ]; then
echo "Aligning geoID 7..."
	#corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid7.geo" -o detectors_file_updated="geometries/geoid7_tel_prealigned.geo" -o histogram_file="geoid7_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid7_tele
		
	#corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid7_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid7_tel_aligned.geo" -o histogram_file="geoid7_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid7_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid7_tel_aligned.geo" -o detectors_file_updated="geometries/geoid7_dut_prealigned.geo" -o histogram_file="geoid7_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid7_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid7_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid7_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid7_dut_aligned.geo" -o histogram_file="geoid7_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid7_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid7_dut
fi

if [ $align_geoid8 -eq 1 ]; then
echo "Aligning geoID 8..."
	#corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid8.geo" -o detectors_file_updated="geometries/geoid8_tel_prealigned.geo" -o histogram_file="geoid8_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid8_tele
		
	#corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid8_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid8_tel_aligned.geo" -o histogram_file="geoid8_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid8_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid8_tel_aligned.geo" -o detectors_file_updated="geometries/geoid8_dut_prealigned.geo" -o histogram_file="geoid8_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid8_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid8_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid8_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid8_dut_aligned.geo" -o histogram_file="geoid8_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid8_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid8_dut
fi

if [ $align_geoid9 -eq 1 ]; then
echo "Aligning geoID 9..."
	corry -c prealign_tel_mpx2.conf -o detectors_file="geometries/geoid9.geo" -o detectors_file_updated="geometries/geoid9_tel_prealigned.geo" -o histogram_file="geoid9_tel_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid9_tele
		
	corry -c align_tel_mpx2.conf -o detectors_file="geometries/geoid9_tel_prealigned.geo" -o detectors_file_updated="geometries/geoid9_tel_aligned.geo" -o histogram_file="geoid9_tel_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid9_tele
	
	corry -c prealign_dut_mpx2.conf -o detectors_file="geometries/geoid9_tel_aligned.geo" -o detectors_file_updated="geometries/geoid9_dut_prealigned.geo" -o histogram_file="geoid9_dut_prealigned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid9_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid9_dut
	
	corry -c align_dut_mpx2.conf -o detectors_file="geometries/geoid9_dut_prealigned.geo" -o detectors_file_updated="geometries/geoid9_dut_aligned.geo" -o histogram_file="geoid9_dut_aligned.root" -o EventLoaderEUDAQ2.file_name=$runfile_geoid9_tele -o EventLoaderEUDAQ2:Monopix2_0.file_name=$runfile_geoid9_dut
fi


exit 0
