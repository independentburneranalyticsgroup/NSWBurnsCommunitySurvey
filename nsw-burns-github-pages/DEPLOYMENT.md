# GitHub Pages Deployment Instructions

## Quick Start (5 minutes)

### Step 1: Create GitHub Repository
1. Go to [GitHub.com](https://github.com) and create a new repository
2. Name it something like `nsw-burns-survey` or `burns-community-results`
3. Make it public (required for free GitHub Pages)
4. Don't initialize with README (we have our own files)

### Step 2: Upload Files
**Option A: Web Interface (Easiest)**
1. Download this entire folder to your computer
2. In your new GitHub repository, click "uploading an existing file"
3. Drag and drop all files from this folder
4. Commit with message: "Initial commit: NSW Burns Survey Interactive Results"

**Option B: Git Command Line**
```bash
# Clone your repository
git clone https://github.com/YOURUSERNAME/YOURREPONAME.git
cd YOURREPONAME

# Copy all files from this folder to your repository folder
# Then commit and push
git add .
git commit -m "Initial commit: NSW Burns Survey Interactive Results"
git push origin main
```

### Step 3: Enable GitHub Pages
1. In your repository, go to **Settings** tab
2. Scroll down to **Pages** section (left sidebar)
3. Under "Source", select **"Deploy from a branch"**
4. Choose **"main"** branch and **"/ (root)"** folder
5. Click **Save**

### Step 4: Access Your Site
- GitHub will provide a URL like: `https://yourusername.github.io/your-repo-name/`
- It may take 2-10 minutes for the site to become available
- Once live, the site will automatically update when you push changes

## Customization Options

### Update Site Title/Description
Edit the `<title>` and `<meta>` tags in `index.html`:
```html
<title>Your Custom Title</title>
<meta name="description" content="Your custom description">
```

### Custom Domain (Optional)
1. Add a `CNAME` file with your domain name
2. Configure DNS with your domain provider
3. Update GitHub Pages settings to use custom domain

### Analytics (Optional)
Add Google Analytics or other tracking code to `index.html` before `</head>`:
```html
<!-- Google Analytics or other tracking code -->
```

## File Structure

```
nsw-burns-github-pages/
├── index.html              # Main HTML file
├── assets/                 # CSS, JS, and other assets
│   ├── index-[hash].css   # Compiled CSS
│   ├── index-[hash].js    # Main JavaScript bundle
│   └── [other-files].js   # Code-split JavaScript files
├── README.md              # Project documentation
├── DEPLOYMENT.md          # This file
└── .gitignore            # Git ignore rules
```

## Troubleshooting

### Site Not Loading
- Wait 10 minutes after enabling GitHub Pages
- Check that repository is public
- Verify all files uploaded correctly
- Check GitHub Pages settings in repository Settings

### Broken Links/Assets
- Ensure all files are in the root directory
- Check that file names match exactly (case-sensitive)
- Verify `index.html` is in the root folder

### Updates Not Showing
- Changes can take 2-10 minutes to appear
- Try hard refresh (Ctrl+F5 or Cmd+Shift+R)
- Check that changes were committed and pushed

## Support

For technical issues:
1. Check GitHub Pages documentation
2. Verify all files are uploaded correctly
3. Ensure repository is public
4. Wait adequate time for deployment (up to 10 minutes)

For content questions, refer to the Independent Burners Analytics Group who conducted the original survey analysis.

## Performance Notes

- Site is optimized for fast loading
- Uses modern web standards
- Responsive design works on all devices
- Accessible design for neurodivergent users
- Code-split for efficient loading

---

**Your NSW Burns Community Survey results will be live and accessible to the world!** 🔥

