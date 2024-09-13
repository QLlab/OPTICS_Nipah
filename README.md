# OPTICS_Nipah
Code for paper "The nanoscale organization of the Nipah virus fusion protein informs new membrane fusion mechanisms"

[Link for paper](https://elifesciences.org/reviewed-preprints/97017v1)

For 3D OPTICS
## Code for "The nanoscale organization of the Nipah virus fusion protein informs new membrane fusion mechanisms"

# SMLM Point Cloud Processing

This project provides tools for processing and analyzing Single Molecule Localization Microscopy (SMLM) point cloud data. It includes implementations of various clustering algorithms such as DBSCAN and OPTICS, as well as utilities for data conversion and visualization.

## Project Structure

The project is organized as follows:

```
├── convert.cpp
├── newCluster.cpp
├── include/
│   ├── PCL_TEST_HEADER.h
│   ├── dbscan.hpp
│   ├── dbscan_kdtree.hpp
│   ├── give_color.hpp
│   ├── optics.hpp
│   ├── optics_new.hpp
│   ├── readmydata.cpp
│   └── statistics.hpp
├── CMakeLists.txt
├── .gitignore
├── test.pcd
└── testdata.pcd
```

## Prerequisites

- CMake (version 3.25 or higher)
- PCL (Point Cloud Library)
- Boost
- Eigen

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/smlm-point-cloud-processing.git
   cd smlm-point-cloud-processing
   ```

2. Create a build directory and navigate to it:
   ```
   mkdir build
   cd build
   ```

3. Run CMake and build the project:
   ```
   cmake ..
   make
   ```

## Usage

After building the project, you can run the main executable:

```
./PCL_test
```

This will process the point cloud data using the OPTICS algorithm and visualize the results.

To convert .3dlp files to .pcd format, use the `PCL_test2` executable:

```
./PCL_test2
```

Make sure to set the correct input folder path in the `convert.cpp` file before running.

## Testdata
The `test.pcd` & `testdata.pcd` are two small datesets for testing and visualization

## License

This project is open-source and available under the [GPL 3.0](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or concerns, please open an issue in the GitHub repository.
