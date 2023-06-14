## Our team(USTH-G8)
|     Members        |    ID    |  
|:------------------:|:--------:|
|  Lê Tuấn Anh       | BA11-005 | 
| Đinh Văn Hiệp      | BA11-041 |  
| Nguyễn Trường Khải | BA11-054 | 
| Lê Vũ Hoàng        | BA11-046 | 
| Nguyễn Nhật Anh    | BI12-022 | 
| Hoàng Trung Kiên   | BA11-059 |
| Nguyễn Hữu Đức     | BA11-025 |
# ## Features
 - Speaker-Recognition
 - GUI, Algorithm, Method

# ##Speaker-Recognition
Automatic Speaker Recognition algorithms in Python

This repository contains Python programs that can be used for Automatic Speaker Recognition. ASR is done by extracting MFCCs and LPCs from each speaker and then forming a speaker-specific codebook
of the same by using Vector Quantization (I like to think of it as a fancy name for NN-clustering). 
After that, the system is trained and tested for 8 different speakers. 

Create virtualenv with:

	virtualenv -p python3 .env
	. .env/bin/activate
	pip install -r requirements.txt

To test the algorithm, run main.py. Certain parameters are open to be changed, such as the order of LPC coefficients, the number of Mel filterbanks and the number of centroids in each codebook.
Everything is included in the repository, including .wav files for testing and training, hence cloning it and running main.py should work. 

A PDF has been included that explains the theory and provides links to relevant websites and projects.
## Step 1: Clone this repository
```
git clone https://github.com/KaiKenju/Speaker-Recognition.git
cd Speaker-Recognition
```
## Step 2: Run the main functions
```
python main.py
```

*if you want to optimize the interface, run the file*

```
GUI.py
```
