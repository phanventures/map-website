import sharp from 'sharp'
import pngToIco from 'png-to-ico'
import { readFileSync, writeFileSync } from 'node:fs'
const OUT = process.argv[2]
const svg = readFileSync(`${OUT}/ap-icon.svg`)
// Full-bleed tile mark: no .trim()/white-square compositing needed (skill's tile exception)
const png = (px) => sharp(svg, { density: 512 }).resize(px, px).png().toBuffer()
for (const [name, px] of [['favicon-16.png',16],['favicon-32.png',32],['apple-touch-icon.png',180],['icon-192.png',192],['icon-512.png',512]]) {
  writeFileSync(`${OUT}/${name}`, await png(px))
}
writeFileSync(`${OUT}/favicon.ico`, await pngToIco([await png(16), await png(32), await png(48)]))
console.log('favicons written')
