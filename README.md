# DuplicatedRemover

중복 이미지 및 PDF 파일을 찾아 제거하는 도구입니다.

## 개요

폴더 내의 중복 이미지와 PDF 파일을 자동으로 감지하고 제거하거나 별도 폴더로 이동시킵니다.

## 주요 기능

- **이미지 중복 검사**: SSIM(Structural Similarity Index)을 사용한 시각적 유사도 검사
- **PDF 중복 검사**: MD5 해시 기반 내용 비교
- **이미지 해시 검사**: perceptual hash를 사용한 이미지 중복 검사
- **선택적 처리**: 삭제 또는 별도 폴더로 이동

## 사용 방법

### 이미지 중복 제거 (DIRemover.py)

```bash
python DIRemover.py
```

실행 후:
1. 검사할 폴더 경로 입력
2. 'move' 또는 'delete' 선택
3. 이동할 경우 대상 폴더 경로 입력

### PDF 중복 제거 (DPDFRemover.py)

```bash
python DPDFRemover.py
```

**주의**: 이 스크립트는 현재 검증되지 않았으므로 사용을 권장하지 않습니다.

## 요구사항

- Python 3.12
- Pillow
- scikit-image
- PyPDF2
- imagehash

## 설치

### uv 설치

#### Windows
```powershell
# PowerShell에서 실행
irm https://astral.sh/uv/install.ps1 | iex
```

#### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 후 터미널을 재시작하거나 다음 명령어로 PATH에 추가:
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### 가상환경 설정

```bash
# Python 3.12 가상환경 생성
uv venv --python 3.12

# 가상환경 활성화
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 패키지 설치

```bash
# uv를 사용한 패키지 설치
uv pip install -r requirements.txt
```

## 파일 구조

- `DIRemover.py`: 이미지 중복 제거 도구
- `DPDFRemover.py`: PDF 중복 제거 도구 (검증 필요)

## 알고리즘

### 이미지 중복 검사
- 이미지를 그레이스케일로 변환
- 100x100 크기로 리사이즈
- SSIM을 사용하여 유사도 계산 (기본 임계값: 0.9)

### PDF 중복 검사
- 각 페이지의 텍스트를 추출
- MD5 해시 생성
- 해시 비교를 통한 중복 검사

---

해당 프로젝트는 Examples-Python의 Private Repository에서 공개 가능한 수준의 소스를 Public Repository로 변환한 것입니다.

