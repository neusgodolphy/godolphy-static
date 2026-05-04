#!/bin/bash
# Download featured images for the 8 new blog posts
# Run from the godolphy-static directory: bash download-blog-images.sh

mkdir -p wp-images

WP_IMAGES_DIR="wp-images"

declare -A IMAGES=(
  ["Group-1000003109-_1_.webp"]="https://www.godolphy.com/wp-content/uploads/2025/05/Group-1000003109-_1_.webp"
  ["professional-girl-manicurist-doing-manicure-and-pa-2024-11-29-23-41-59-utc-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/professional-girl-manicurist-doing-manicure-and-pa-2024-11-29-23-41-59-utc-scaled.jpg"
  ["process-of-manicure-at-beuaty-with-two-attractive-2025-01-26-04-28-21-utc-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/process-of-manicure-at-beuaty-with-two-attractive-2025-01-26-04-28-21-utc-scaled.jpg"
  ["cheerful-manicurist-is-posing-for-photographer-2023-11-27-05-04-50-utc-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/cheerful-manicurist-is-posing-for-photographer-2023-11-27-05-04-50-utc-scaled.jpg"
  ["hairstylist-trimming-hair-of-the-customer-in-a-bea-2025-02-09-23-28-24-utc-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/hairstylist-trimming-hair-of-the-customer-in-a-bea-2025-02-09-23-28-24-utc-scaled.jpg"
  ["male-having-nails-and-hair-treatment-in-beauty-sal-2023-11-27-05-29-08-utc-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/male-having-nails-and-hair-treatment-in-beauty-sal-2023-11-27-05-29-08-utc-scaled.jpg"
  ["barberis-alta-aeat-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/barberis-alta-aeat-scaled.jpg"
  ["grooming-studio-with-stylist-caring-dog-2024-06-21-01-43-51-utc-scaled.jpg"]="https://www.godolphy.com/wp-content/uploads/2025/02/grooming-studio-with-stylist-caring-dog-2024-06-21-01-43-51-utc-scaled.jpg"
)

for FILENAME in "${!IMAGES[@]}"; do
  URL="${IMAGES[$FILENAME]}"
  DEST="$WP_IMAGES_DIR/$FILENAME"
  if test -f "$DEST"; then
    echo "Already exists: $FILENAME"
  else
    echo "Downloading: $FILENAME"
    curl -L -o "$DEST" "$URL" && echo "Done: $FILENAME" || echo "FAILED: $FILENAME"
  fi
done

echo ""
echo "All done. Images saved to wp-images/"
