import re

file_path = 'c:/NAB TRAVELS/index.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Swiper CSS in head
if 'swiper-bundle.min.css' not in content:
    content = content.replace('    <link rel="stylesheet" href="style.css">', '    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />\n    <link rel="stylesheet" href="style.css">')

# 2. Add Swiper JS before </body>
if 'swiper-bundle.min.js' not in content:
    swiper_script = """
    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var swiper = new Swiper('.advance-swiper', {
                slidesPerView: 4,
                spaceBetween: 30,
                loop: true,
                slidesPerGroup: 1,
                autoplay: {
                    delay: 2500,
                    disableOnInteraction: false,
                },
                breakpoints: {
                    320: { slidesPerView: 1 },
                    768: { slidesPerView: 2 },
                    992: { slidesPerView: 3 },
                    1200: { slidesPerView: 4 }
                }
            });
            
            // Pause on hover
            const swiperContainer = document.querySelector('.advance-swiper');
            if(swiperContainer) {
                swiperContainer.addEventListener('mouseenter', function() {
                    swiper.autoplay.stop();
                });
                swiperContainer.addEventListener('mouseleave', function() {
                    swiper.autoplay.start();
                });
            }
        });
    </script>
"""
    content = content.replace('</body>', swiper_script + '</body>')

# 3. Update HTML structure for advance-grid
# Wrap .advance-grid in .swiper .advance-swiper
if 'class="swiper advance-swiper"' not in content:
    content = content.replace('<div class="advance-grid">', '<div class="swiper advance-swiper">\n                <div class="swiper-wrapper advance-grid">')
    # Close the swiper div after advance-grid
    content = content.replace('</div>\n        </div>\n    </section>', '</div>\n            </div>\n        </div>\n    </section>')
    
    # Add swiper-slide class to all advance-card
    content = content.replace('class="advance-card"', 'class="swiper-slide advance-card"')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Swiper applied successfully to index.html!")
