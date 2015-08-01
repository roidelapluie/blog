#!/bin/bash
./git-arr/git-arr --config git-arr.cfg generate --output git
rsync -r git/ git-output-$1
find git -name '*.html' -print0 | xargs -P 4 -I K -0 bash transform.sh  K $1
cat git-arr/static/git-arr.css |sed '/^[a-z]/s/\(^\|, \)/&.git /g' > git-output-$1/static/git-arr.css

