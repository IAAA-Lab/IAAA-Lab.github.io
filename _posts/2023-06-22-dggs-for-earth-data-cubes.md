---
title: Discrete Global Grid Systems with Quadrangular Cells as Reference Frameworks for the Current Generation of Earth Observation Data Cubes
subtitle:
layout: post
categories: [Paper overview]
---

Discrete global grid systems (DGGSs) are spatial reference frameworks that associate information to multi-resolution grids of uniquely identified cells. In simpler terms, DGGSs divide the whole surface of the Earth into non-overlapping cells, each with a unique identifier. The main advantage of DGGSs over traditional geographic projections is that they do not have any singularities, that all the cells in a certain resolution are equal-area, what makes it easier and faster to carry out many common spatial computations, and that they work well for very large areas, or even for the whole Earth. We have used the [rHEALPix DGGS](https://iopscience.iop.org/article/10.1088/1755-1315/34/1/012012) as shown in Figure 2.

![Figure 2: (1,0)-rHEALPix resolution 1 cells with Nside = 3 and prime meridian at 10º]({{ site.baseurl }}/images/posts/2023-06-22-fig2-rHEALPixWorld.png){: .center-image width="80%"}

In this research, we have investigated how discrete global grid systems with quadrangular cells can be a useful approach to process large-scale Earth observation (EO) datasets. Earth observation data cubes are data processing infrastructures, focused on remotely sensed EO (mostly satellite) data. They organize EO data in n-dimensional arrays, the cubes, along dimensions such as longitude, latitude, time or spectral bands. They make it easy for geodata analysts to request the data of interest by slicing those cubes, without worrying about the infrastructure that makes it possible to do so efficiently and easily for the usually very large datasets they are working with. We have used [Open Data Cube](https://www.opendatacube.org) in our experiments.

We have found that certain pre-processing steps allow us to use current EO data cubes to process any dataset within some DGGSs. The most relevant point is that this doesn't require any technological advancements on the data cube side, making it easy to integrate this in current deployments. We test this approach on typical datasets required for EO applications, thus showing its practical relevance as well as the validity of this approach (Figure 4 shows the very small differences produced by the two different solutions, without and with the DGGS). Additionally, we describe some technical challenges that we faced and the solutions we took.

![Figure 4: Pyrenees. Absolute difference in snow cover between the UTM 30N and the rHEALPix datasets. Mollweide projection.]({{ site.baseurl }}/images/posts/2023-06-22-fig4_pyrenees_utm_rhealpix.png){:.center-image width="80%"}

This paper shows that some DGGSs can be easily integrated into the current generation of Earth observation data cubes. This, plus the fact that cells in DGGSs have unique identifiers, and thus can be seen as entities in any information system, opens the possibility to a seamless, fast, lossless interoperability between data cubes on the one hand, and databases and data warehouses on the other hand. And all this while allowing the current data analysts working on this very different infrastructures to keep using ther preferred tools on the platforms they already know. 

---
[Discrete Global Grid Systems with quadrangular cells as reference frameworks for the current generation of Earth observation data cubes.](https://doi.org/10.1016/j.envsoft.2023.105656) R. BÉJAR, J. LACASTA, F.J. LOPEZ-PELLICER, J. NOGUERAS-ISO. *Environmental Modelling & Software*, 162 (2023) 105656, 2023.


*The code and datasets are in [GitHub](https://github.com/IAAA-Lab/rhealpix-opendatacube-docker).*

---
