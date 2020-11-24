
- [projectq Benchmark Results](#projectq-benchmark-results)
  - [Module Info](#module-info)
  - [Hardware Platform](#hardware-platform)
  - [LiH molecule](#lih-molecule)
    - [Settings](#settings)
    - [Result](#result)
  - [BeH2 molecule](#beh2-molecule)
    - [Settings](#settings-1)
    - [Result](#result-1)
  - [H2O molecule](#h2o-molecule)
    - [Settings](#settings-2)
    - [Result](#result-2)
  - [N2 molecule](#n2-molecule)
    - [Settings](#settings-3)
    - [Result](#result-3)
- [Contributor](#contributor)

# projectq Benchmark Results
The performance of different algorithms in projectq for different molecules

## Module Info
| Module |    Name    |   WebPage |
|:-------:|:-------:|:-------------:|
| Molecule Modeling | PySCF | https://github.com/pyscf/pyscf |
| Quantum simulator |   projectq  |        |
| VQE algorithm | openfermion |  |

## Hardware Platform
```
HUAWEI server
Taiyi HPC
```

## LiH molecule
### Settings
```
 Basis: STO-3G
 Transformation:Jordan-Wigner
 Qubit number: 12
```

### Result
![image](https://github.com/CopperHu/VQE-Benchmark/raw/master/images/LiH.png )

## BeH2 molecule
### Settings
```
 Basis: STO-3G
 Transformation:Jordan-Wigner
 Qubit number: 14
```

### Result
![image](https://github.com/CopperHu/VQE-Benchmark/raw/master/images/BeH2.png )

## H2O molecule
### Settings
```
 Basis: STO-3G
 Transformation:Jordan-Wigner
 Qubit number: 14
```

### Result
![image](https://github.com/CopperHu/VQE-Benchmark/raw/master/images/h2o.png )

## N2 molecule
### Settings
```
 Basis: STO-3G
 Transformation:Jordan-Wigner
 Qubit number: 20
```

### Result
![image](https://github.com/CopperHu/VQE-Benchmark/raw/master/images/h2o.png )

# Contributor
Benchmark and Document writing: Jiaqi Hu 
