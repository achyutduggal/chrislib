# setup.py for chrislib repo
import setuptools
setuptools.setup(
    name="chrislib",
    version="0.0.1",
    author="Chris Careaga",
    author_email="careagc256@gmail.com",
    description="",
    url="",
    packages=setuptools.find_packages(),
    license="",
    python_requires=">=3.8",
    install_requires=[
        # Core dependencies with exact versions
        'numpy==1.26.4',
        'opencv-python==4.11.0.86',
        
        # PyTorch ecosystem - CUDA 12.4 compatible versions
        'torch>=2.4.0,<2.5.0',
        'torchvision>=0.19.0,<0.20.0',
        'torchaudio>=2.4.0,<2.5.0',
        'kornia>=0.7.3,<0.8.0',  # Updated for PyTorch 2.4 compatibility
        
        # Image processing - use ranges for flexibility
        'Pillow>=9.4.0,<11.0.0',
        'imageio>=2.31.0,<3.0.0',
        'scikit-image>=0.19.0,<0.22.0',
        
        # Web/parsing libraries - more flexible
        'beautifulsoup4>=4.11.0,<5.0.0',
        'requests>=2.31.0,<3.0.0',
        
        # Scientific computing
        'scipy>=1.10.0,<1.11.0',
        'matplotlib>=3.7.0,<3.8.0',
        
        # Utilities
        'tqdm>=4.66.0,<5.0.0',
        'gdown>=4.7.0,<5.0.0'
    ]
)
