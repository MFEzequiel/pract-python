"use strict"
import { $, d, $$, cr, cl } from './jQuery.js'

const filtered = $('.filter')
const containerFilter = $('.filterabled')
const frut = ['Banana', 'Naranja', 'Pera']
const filt = frut.filter(el => el.toLowerCase() === filtered.value.toLowerCase())
const p = d.createElement('p')

filtered.addEventListener('change', update)

function update() {
  filt.map(el => p.textContent = el)
  
  if (p.textContent !== '') {
    containerFilter.appendChild(p)
  }
  
}

// cl(filt)
// cl(filtered.value)