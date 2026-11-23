# -*- coding: utf-8 -*-
import os, base64, subprocess

base_dir = '/Users/green/Downloads/Takealot Smart TV - Copia'
img_dir = os.path.join(base_dir, 'imagens')
out_dir = os.path.join(base_dir, 'creatives')
artifact_dir = '/Users/green/.gemini/antigravity/brain/72c774ca-b661-487e-a546-a76e2b7f9ea4'
os.makedirs(out_dir, exist_ok=True)
os.makedirs(artifact_dir, exist_ok=True)

def b64(filename):
    p = os.path.join(img_dir, filename)
    with open(p, 'rb') as f:
        data = base64.b64encode(f.read()).decode('utf-8')
    ext = filename.split('.')[-1].lower()
    mime = 'image/png' if ext == 'png' else 'image/jpeg'
    return f"data:{mime};base64,{data}"

logo_b64 = b64('Takealot_logo.svg.png')
tv1_b64 = b64('tv_65_1.png')
tv3_b64 = b64('tv_65_3.png')
tv5_b64 = b64('tv_65_5.png')
tv_bundle_b64 = b64('tv_bundle_1.png')
cards_b64 = b64('cards_accepted.png')

# ----------------------------------------------------------------------
# CREATIVE 1: High-Impact Direct Response Feed Ad (1080x1080)
# ----------------------------------------------------------------------
html_c1 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: radial-gradient(circle at 50% 35%, #152846 0%, #081224 60%, #030811 100%);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #fff;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0;
  }}

  /* Top Urgency Header */
  .top-banner {{
    background: linear-gradient(90deg, #ff0055 0%, #ff5500 50%, #ff0055 100%);
    color: #ffffff;
    text-align: center;
    padding: 14px 20px;
    font-size: 21px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 4px 20px rgba(255, 85, 0, 0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
  }}

  /* Brand & Deals Header */
  .header-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 50px 0 50px;
  }}
  .brand-logo {{
    height: 52px;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
  }}
  .badge-tag {{
    background: rgba(11, 121, 191, 0.25);
    border: 1.5px solid #0b79bf;
    color: #38bdf8;
    padding: 8px 18px;
    border-radius: 30px;
    font-size: 17px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}

  /* Main Product Title */
  .title-area {{
    text-align: center;
    padding: 10px 40px 0 40px;
  }}
  .product-title {{
    font-size: 48px;
    font-weight: 900;
    line-height: 1.15;
    letter-spacing: -0.5px;
    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .product-sub {{
    font-size: 20px;
    color: #94a3b8;
    margin-top: 6px;
    font-weight: 600;
  }}

  /* Center Product Visual */
  .visual-area {{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 480px;
    margin-top: -10px;
  }}
  .glow-backdrop {{
    position: absolute;
    width: 600px;
    height: 350px;
    background: radial-gradient(circle, rgba(11, 121, 191, 0.45) 0%, rgba(14, 165, 233, 0.1) 50%, transparent 70%);
    filter: blur(40px);
    z-index: 1;
  }}
  .tv-image {{
    max-height: 440px;
    max-width: 820px;
    object-fit: contain;
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 25px 40px rgba(0,0,0,0.85));
  }}

  /* Specs Pills */
  .specs-row {{
    display: flex;
    justify-content: center;
    gap: 14px;
    margin-top: -15px;
    z-index: 3;
    padding: 0 40px;
  }}
  .spec-pill {{
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 9px 18px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 700;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .spec-pill span {{
    color: #38bdf8;
  }}

  /* Bottom Conversion Area */
  .bottom-box {{
    background: rgba(15, 23, 42, 0.85);
    border-top: 1.5px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(20px);
    padding: 26px 50px 32px 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    z-index: 3;
  }}
  .price-col {{
    display: flex;
    flex-direction: column;
  }}
  .old-price {{
    font-size: 22px;
    color: #94a3b8;
    text-decoration: line-through;
    font-weight: 600;
  }}
  .now-row {{
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-top: 2px;
  }}
  .now-price {{
    font-size: 64px;
    font-weight: 900;
    color: #22c55e;
    letter-spacing: -1.5px;
    line-height: 1;
    text-shadow: 0 4px 20px rgba(34, 197, 94, 0.35);
  }}
  .discount-pill {{
    background: #ef4444;
    color: #fff;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: 900;
    letter-spacing: 0.5px;
  }}
  .shipping-text {{
    font-size: 15px;
    color: #38bdf8;
    font-weight: 700;
    margin-top: 6px;
    display: flex;
    align-items: center;
    gap: 6px;
  }}

  .cta-col {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
  }}
  .cta-btn {{
    background: linear-gradient(135deg, #0b79bf 0%, #0284c7 100%);
    color: #ffffff;
    font-size: 24px;
    font-weight: 900;
    padding: 18px 40px;
    border-radius: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 10px 30px rgba(11, 121, 191, 0.5);
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .trust-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    color: #94a3b8;
    font-weight: 600;
  }}
  .stars {{
    color: #fbbf24;
    font-size: 16px;
  }}
</style>
</head>
<body>
  <div class="top-banner">
    <span>⚡</span> BLACK NOVEMBER PROMOTIONAL CLEARANCE &bull; LIMITED WAREHOUSE UNITS <span>⚡</span>
  </div>

  <div class="header-row">
    <img src="{logo_b64}" class="brand-logo" alt="Takealot.com" />
    <div class="badge-tag">Verified Official Deal</div>
  </div>

  <div class="title-area">
    <h1 class="product-title">Hisense 65" 4K QLED Smart TV</h1>
    <div class="product-sub">Series E7Q &bull; Quantum Dot Technology &bull; HDR10+ &bull; Dolby Atmos</div>
  </div>

  <div class="visual-area">
    <div class="glow-backdrop"></div>
    <img src="{tv1_b64}" class="tv-image" alt="Hisense 65 Smart TV" />
  </div>

  <div class="specs-row">
    <div class="spec-pill"><span>✓</span> 4K Ultra HD QLED</div>
    <div class="spec-pill"><span>✓</span> Dolby Vision & Atmos</div>
    <div class="spec-pill"><span>✓</span> Game Mode Plus 120Hz</div>
    <div class="spec-pill"><span>✓</span> VIDAA Smart OS</div>
  </div>

  <div class="bottom-box">
    <div class="price-col">
      <div class="old-price">Retail Price: R 12,999</div>
      <div class="now-row">
        <div class="now-price">R 1,199</div>
        <div class="discount-pill">-90% OFF</div>
      </div>
      <div class="shipping-text">🚚 FREE 24-48h Nationwide Delivery Included</div>
    </div>
    <div class="cta-col">
      <div class="cta-btn">BUY ON TAKEALOT &rarr;</div>
      <div class="trust-row">
        <span class="stars">★★★★★</span>
        <span>4.8/5 Rating &bull; 3,420+ Verified Buyers</span>
      </div>
    </div>
  </div>
</body>
</html>
"""

# ----------------------------------------------------------------------
# CREATIVE 2: Modern Living Room Lifestyle Experience (1080x1080)
# ----------------------------------------------------------------------
html_c2 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: #0f172a;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #fff;
    overflow: hidden;
    position: relative;
  }}

  /* Full Background Image */
  .lifestyle-bg {{
    position: absolute;
    top: 0;
    left: 0;
    width: 1080px;
    height: 1080px;
    object-fit: cover;
    z-index: 1;
    filter: brightness(0.92) contrast(1.05);
  }}

  /* Dark Vignette Overlay */
  .vignette {{
    position: absolute;
    top: 0;
    left: 0;
    width: 1080px;
    height: 1080px;
    background: linear-gradient(180deg, rgba(8, 15, 28, 0.82) 0%, rgba(8, 15, 28, 0.1) 40%, rgba(8, 15, 28, 0.92) 85%);
    z-index: 2;
  }}

  /* Top Navigation / Brand */
  .top-bar {{
    position: absolute;
    top: 40px;
    left: 50px;
    right: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
  }}
  .logo-pill {{
    background: rgba(255, 255, 255, 0.95);
    padding: 10px 22px;
    border-radius: 30px;
    display: flex;
    align-items: center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
  }}
  .logo-pill img {{
    height: 38px;
  }}
  .urgency-badge {{
    background: #dc2626;
    color: #fff;
    padding: 12px 24px;
    border-radius: 30px;
    font-size: 16px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
    box-shadow: 0 4px 20px rgba(220, 38, 38, 0.5);
    animation: pulse 2s infinite;
  }}

  /* Floating Spec Card (Middle Left) */
  .spec-floating-card {{
    position: absolute;
    top: 170px;
    left: 50px;
    z-index: 10;
    max-width: 460px;
  }}
  .headline {{
    font-size: 44px;
    font-weight: 900;
    line-height: 1.15;
    text-shadow: 0 4px 15px rgba(0,0,0,0.8);
  }}
  .headline span {{
    color: #38bdf8;
  }}
  .sub-headline {{
    font-size: 19px;
    color: #e2e8f0;
    margin-top: 10px;
    line-height: 1.4;
    text-shadow: 0 2px 10px rgba(0,0,0,0.8);
  }}

  /* Bottom Floating Offer Card */
  .offer-card {{
    position: absolute;
    bottom: 50px;
    left: 50px;
    right: 50px;
    background: rgba(15, 23, 42, 0.88);
    backdrop-filter: blur(25px);
    border: 1.5px solid rgba(255, 255, 255, 0.18);
    border-radius: 24px;
    padding: 26px 36px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 10;
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  }}
  .offer-info {{
    display: flex;
    flex-direction: column;
  }}
  .deal-tag {{
    font-size: 14px;
    font-weight: 800;
    color: #fbbf24;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 4px;
  }}
  .price-wrapper {{
    display: flex;
    align-items: baseline;
    gap: 14px;
  }}
  .price-tag {{
    font-size: 60px;
    font-weight: 900;
    color: #22c55e;
    line-height: 1;
    text-shadow: 0 4px 15px rgba(34, 197, 94, 0.3);
  }}
  .was-price {{
    font-size: 20px;
    color: #94a3b8;
    text-decoration: line-through;
    font-weight: 600;
  }}
  .perks-row {{
    display: flex;
    gap: 16px;
    margin-top: 8px;
    font-size: 14px;
    color: #cbd5e1;
    font-weight: 600;
  }}

  .cta-action {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 8px;
  }}
  .main-cta {{
    background: #0b79bf;
    background: linear-gradient(135deg, #0b79bf 0%, #0369a1 100%);
    color: #ffffff;
    font-size: 22px;
    font-weight: 900;
    padding: 18px 36px;
    border-radius: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 10px 25px rgba(11, 121, 191, 0.5);
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .security-note {{
    font-size: 13px;
    color: #94a3b8;
  }}
</style>
</head>
<body>
  <img src="{tv5_b64}" class="lifestyle-bg" alt="Hisense Living Room Setup" />
  <div class="vignette"></div>

  <div class="top-bar">
    <div class="logo-pill">
      <img src="{logo_b64}" alt="Takealot" />
    </div>
    <div class="urgency-badge">🔥 Only 14 Units at R 1,199</div>
  </div>

  <div class="spec-floating-card">
    <h2 class="headline">Upgrade to <span>Cinema-Grade 4K QLED</span></h2>
    <p class="sub-headline">Experience 1 Billion+ colors, Dolby Vision HDR & immersive cinema sound in the comfort of your living room.</p>
  </div>

  <div class="offer-card">
    <div class="offer-info">
      <div class="deal-tag">Takealot Exclusive Clearance</div>
      <div class="price-wrapper">
        <div class="price-tag">R 1,199</div>
        <div class="was-price">Was R 12,999</div>
      </div>
      <div class="perks-row">
        <div>🚚 Free Door Delivery</div>
        <div>🛡️ 2-Year Official Guarantee</div>
        <div>⭐ 4.8 / 5 Rating</div>
      </div>
    </div>
    <div class="cta-action">
      <div class="main-cta">CLAIM YOURS NOW &rarr;</div>
      <div class="security-note">Pay with Credit/Debit Card &bull; 100% Protected</div>
    </div>
  </div>
</body>
</html>
"""

# ----------------------------------------------------------------------
# CREATIVE 3: Ultimate Bundle Offer (TV + Soundbar) (1080x1080)
# ----------------------------------------------------------------------
html_c3 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1080px;
    background: radial-gradient(circle at 50% 40%, #1e1b4b 0%, #0f172a 55%, #020617 100%);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #fff;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}

  /* Top Ribbon */
  .bundle-ribbon {{
    background: linear-gradient(90deg, #7c3aed 0%, #9333ea 50%, #c026d3 100%);
    color: #ffffff;
    text-align: center;
    padding: 14px 20px;
    font-size: 21px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 4px 25px rgba(147, 51, 234, 0.4);
  }}

  .header-box {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 24px 50px 0 50px;
  }}
  .takealot-logo {{
    height: 48px;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.5));
  }}
  .bundle-badge {{
    background: #facc15;
    color: #0f172a;
    font-size: 16px;
    font-weight: 900;
    padding: 8px 18px;
    border-radius: 8px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }}

  .hero-titles {{
    text-align: center;
    padding: 10px 40px 0 40px;
  }}
  .h-main {{
    font-size: 46px;
    font-weight: 900;
    line-height: 1.15;
    background: linear-gradient(180deg, #ffffff 0%, #e2e8f0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .h-sub {{
    font-size: 22px;
    color: #c084fc;
    font-weight: 800;
    margin-top: 6px;
  }}

  /* Center Visual with Bundle */
  .bundle-visual {{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 480px;
    margin-top: -10px;
  }}
  .glow-purple {{
    position: absolute;
    width: 650px;
    height: 380px;
    background: radial-gradient(circle, rgba(147, 51, 234, 0.4) 0%, rgba(99, 102, 241, 0.1) 50%, transparent 70%);
    filter: blur(45px);
    z-index: 1;
  }}
  .bundle-img {{
    max-height: 450px;
    max-width: 860px;
    object-fit: contain;
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 25px 40px rgba(0,0,0,0.85));
  }}

  /* What is Included Tag */
  .included-strip {{
    display: flex;
    justify-content: center;
    gap: 16px;
    margin-top: -20px;
    z-index: 3;
    padding: 0 40px;
  }}
  .included-item {{
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 8px 16px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
    color: #f1f5f9;
  }}
  .included-item span {{
    color: #4ade80;
  }}

  /* Bottom Conversion Area */
  .bundle-bottom {{
    background: rgba(15, 23, 42, 0.9);
    border-top: 1.5px solid rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(20px);
    padding: 24px 50px 30px 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 3;
  }}
  .bundle-pricing {{
    display: flex;
    flex-direction: column;
  }}
  .val-row {{
    font-size: 20px;
    color: #94a3b8;
    text-decoration: line-through;
    font-weight: 600;
  }}
  .main-val-row {{
    display: flex;
    align-items: baseline;
    gap: 12px;
    margin-top: 2px;
  }}
  .bundle-price {{
    font-size: 64px;
    font-weight: 900;
    color: #facc15;
    letter-spacing: -1.5px;
    line-height: 1;
    text-shadow: 0 4px 20px rgba(250, 204, 21, 0.35);
  }}
  .save-tag {{
    background: #22c55e;
    color: #0f172a;
    padding: 6px 14px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 900;
  }}
  .bundle-delivery {{
    font-size: 15px;
    color: #38bdf8;
    font-weight: 700;
    margin-top: 6px;
  }}

  .bundle-cta-box {{
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 10px;
  }}
  .bundle-cta {{
    background: linear-gradient(135deg, #9333ea 0%, #7c3aed 100%);
    color: #ffffff;
    font-size: 24px;
    font-weight: 900;
    padding: 18px 40px;
    border-radius: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    box-shadow: 0 10px 30px rgba(147, 51, 234, 0.5);
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .guarantee-text {{
    font-size: 14px;
    color: #94a3b8;
    font-weight: 600;
  }}
</style>
</head>
<body>
  <div class="bundle-ribbon">
    🎁 2-IN-1 HOME THEATER BUNDLE DEAL &bull; COMPLETE CINEMA EXPERIENCE
  </div>

  <div class="header-box">
    <img src="{logo_b64}" class="takealot-logo" alt="Takealot.com" />
    <div class="bundle-badge">⚡ MEGA COMBO DISCOUNT</div>
  </div>

  <div class="hero-titles">
    <h1 class="h-main">Hisense 65" 4K QLED + 2.1ch Dolby Soundbar</h1>
    <div class="h-sub">Everything Included: 65-Inch Smart TV + Wireless Soundbar & Subwoofer</div>
  </div>

  <div class="bundle-visual">
    <div class="glow-purple"></div>
    <img src="{tv_bundle_b64}" class="bundle-img" alt="TV and Soundbar Bundle" />
  </div>

  <div class="included-strip">
    <div class="included-item"><span>✓</span> Hisense 65" 4K QLED TV</div>
    <div class="included-item"><span>✓</span> 2.1ch Wireless Soundbar</div>
    <div class="included-item"><span>✓</span> Deep Bass Subwoofer</div>
    <div class="included-item"><span>✓</span> Dual Remote Controls</div>
  </div>

  <div class="bundle-bottom">
    <div class="bundle-pricing">
      <div class="val-row">Total Retail Value: R 17,499</div>
      <div class="main-val-row">
        <div class="bundle-price">R 1,499</div>
        <div class="save-tag">SAVE R 16,000</div>
      </div>
      <div class="bundle-delivery">🚚 FREE Express Courier Delivery to Your Door</div>
    </div>
    <div class="bundle-cta-box">
      <div class="bundle-cta">GET THE BUNDLE NOW &rarr;</div>
      <div class="guarantee-text">🛡️ 2-Year Official Warranty &bull; Limited Warehouse Units</div>
    </div>
  </div>
</body>
</html>
"""

# ----------------------------------------------------------------------
# CREATIVE 4: Instagram / Facebook Story & Reels Vertical (1080x1920)
# ----------------------------------------------------------------------
html_c4 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1080px;
    height: 1920px;
    background: radial-gradient(circle at 50% 30%, #172554 0%, #0b1528 50%, #020617 100%);
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    color: #fff;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0;
  }}

  /* Top Story Header */
  .story-top {{
    padding: 60px 50px 0 50px;
    text-align: center;
    position: relative;
    z-index: 10;
  }}
  .flash-pill {{
    display: inline-block;
    background: linear-gradient(90deg, #ef4444 0%, #f97316 100%);
    color: #ffffff;
    padding: 12px 30px;
    border-radius: 40px;
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow: 0 4px 20px rgba(239, 68, 68, 0.5);
    margin-bottom: 24px;
  }}
  .story-logo {{
    height: 56px;
    display: block;
    margin: 0 auto 20px auto;
    filter: drop-shadow(0 4px 15px rgba(0,0,0,0.6));
  }}
  .story-title {{
    font-size: 64px;
    font-weight: 900;
    line-height: 1.1;
    letter-spacing: -1px;
    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .story-subtitle {{
    font-size: 26px;
    color: #38bdf8;
    font-weight: 700;
    margin-top: 10px;
  }}

  /* Middle TV Visual Stage */
  .story-visual-stage {{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 720px;
    margin-top: -30px;
  }}
  .ambient-glow {{
    position: absolute;
    width: 700px;
    height: 500px;
    background: radial-gradient(circle, rgba(11, 121, 191, 0.5) 0%, rgba(56, 189, 248, 0.15) 50%, transparent 75%);
    filter: blur(50px);
    z-index: 1;
  }}
  .tv-hero-story {{
    max-height: 640px;
    max-width: 980px;
    object-fit: contain;
    position: relative;
    z-index: 2;
    filter: drop-shadow(0 30px 60px rgba(0,0,0,0.9));
  }}

  /* Feature Grid Cards */
  .story-features {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    padding: 0 60px;
    margin-top: -20px;
    z-index: 10;
  }}
  .feat-card {{
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(15px);
    border: 1px solid rgba(255, 255, 255, 0.14);
    border-radius: 18px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .feat-icon {{
    font-size: 28px;
  }}
  .feat-text-title {{
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
  }}
  .feat-text-sub {{
    font-size: 14px;
    color: #94a3b8;
    margin-top: 2px;
  }}

  /* Bottom Conversion Action Container */
  .story-bottom {{
    background: rgba(15, 23, 42, 0.95);
    border-top: 2px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(30px);
    padding: 40px 60px 70px 60px;
    z-index: 10;
  }}
  .price-highlight-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }}
  .st-price-col {{
    display: flex;
    flex-direction: column;
  }}
  .st-old {{
    font-size: 26px;
    color: #94a3b8;
    text-decoration: line-through;
    font-weight: 600;
  }}
  .st-new {{
    font-size: 76px;
    font-weight: 900;
    color: #22c55e;
    letter-spacing: -2px;
    line-height: 1;
    margin-top: 4px;
    text-shadow: 0 4px 25px rgba(34, 197, 94, 0.4);
  }}
  .st-discount-badge {{
    background: #ef4444;
    color: #ffffff;
    font-size: 26px;
    font-weight: 900;
    padding: 14px 24px;
    border-radius: 16px;
    box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
  }}

  /* Massive CTA Button */
  .story-cta-btn {{
    background: linear-gradient(135deg, #0b79bf 0%, #0284c7 100%);
    color: #ffffff;
    font-size: 32px;
    font-weight: 900;
    text-align: center;
    padding: 26px 40px;
    border-radius: 20px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    box-shadow: 0 15px 40px rgba(11, 121, 191, 0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 14px;
  }}
  .swipe-indicator {{
    text-align: center;
    font-size: 17px;
    color: #94a3b8;
    font-weight: 700;
    margin-top: 18px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
</style>
</head>
<body>
  <div class="story-top">
    <div class="flash-pill">⚡ BLACK NOVEMBER FLASH DROP ⚡</div>
    <img src="{logo_b64}" class="story-logo" alt="Takealot" />
    <h1 class="story-title">Hisense 65" 4K QLED</h1>
    <div class="story-subtitle">Series E7Q &bull; Quantum Dot Technology</div>
  </div>

  <div class="story-visual-stage">
    <div class="ambient-glow"></div>
    <img src="{tv1_b64}" class="tv-hero-story" alt="Hisense Smart TV" />
  </div>

  <div class="story-features">
    <div class="feat-card">
      <div class="feat-icon">✨</div>
      <div>
        <div class="feat-text-title">Quantum Dot 4K</div>
        <div class="feat-text-sub">1 Billion+ Vibrant Colors</div>
      </div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🔊</div>
      <div>
        <div class="feat-text-title">Dolby Vision & Atmos</div>
        <div class="feat-text-sub">Cinema Visuals & Audio</div>
      </div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🎮</div>
      <div>
        <div class="feat-text-title">Game Mode Plus</div>
        <div class="feat-text-sub">Ultra-low Lag & 120Hz</div>
      </div>
    </div>
    <div class="feat-card">
      <div class="feat-icon">🚚</div>
      <div>
        <div class="feat-text-title">Fast Delivery</div>
        <div class="feat-text-sub">Free Across South Africa</div>
      </div>
    </div>
  </div>

  <div class="story-bottom">
    <div class="price-highlight-row">
      <div class="st-price-col">
        <div class="st-old">Retail: R 12,999</div>
        <div class="st-new">R 1,199</div>
      </div>
      <div class="st-discount-badge">-90% OFF</div>
    </div>

    <div class="story-cta-btn">
      <span>SWIPE UP &bull; ORDER NOW</span>
      <span>&rarr;</span>
    </div>

    <div class="swipe-indicator">
      👆 TAP OR SWIPE UP TO CLAIM YOUR DEAL &bull; ONLY 14 LEFT
    </div>
  </div>
</body>
</html>
"""

creatives = [
    ('creative_1_takealot_deal.html', 'creative_1_takealot_deal.png', 1080, 1080, html_c1),
    ('creative_2_living_room_lifestyle.html', 'creative_2_living_room_lifestyle.png', 1080, 1080, html_c2),
    ('creative_3_bundle_value.html', 'creative_3_bundle_value.png', 1080, 1080, html_c3),
    ('creative_4_story_9x16.html', 'creative_4_story_9x16.png', 1080, 1920, html_c4)
]

for html_name, png_name, w, h, content in creatives:
    html_file = os.path.join(out_dir, html_name)
    png_file = os.path.join(out_dir, png_name)
    artifact_png = os.path.join(artifact_dir, png_name)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Rendering {png_name} ({w}x{h})...")
    subprocess.run([
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '--headless',
        '--disable-gpu',
        f'--screenshot={png_file}',
        f'--window-size={w},{h}',
        '--hide-scrollbars',
        f'file://{html_file}'
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Also copy to artifact directory for presentation
    if os.path.exists(png_file):
        import shutil
        shutil.copy2(png_file, artifact_png)
        print(f"  -> Generated {png_file} ({os.path.getsize(png_file)} bytes)")

print("All 4 creatives successfully generated!")
