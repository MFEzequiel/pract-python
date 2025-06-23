"use strict";
import {$, d, $$, cr, cl } from './jQuery.js'

// User theme
let currentTheme = 'light'
const themeToggleButton = $('.theme')
const htmlElement = document.documentElement

function upadateTheme () {

  if (
    window.matchMedia &&
    window.matchMedia('(prefers-color-scheme: dark)').matches
  ) {
    return 'dark'
  } else {
    return 'light'
  }
}

function applyTheme(newTheme) {
  htmlElement.setAttribute('data-theme', newTheme)
}

themeToggleButton.addEventListener('click', () => {
  
  currentTheme = currentTheme === 'light' ? 'dark' : 'light'
  
  applyTheme(currentTheme)
})

window
.matchMedia(`(prefers-color-scheme: dark)`)
  .addEventListener('change', () => applyTheme(upadateTheme()));

applyTheme(upadateTheme())

// Variables selector css
const form = $('.form')
const ip = $('.search') 
const bt = $('.bt')
const ul = $('.ul')
const li = cr('li')

async function fetchData() {
    try {
        let res = await fetch('http://localhost:3000/product')
        
        if (!res.ok) {
            throw new Error('Erro al solicitar los productos')
        }
    
        let data = await res.json()
        
        data.Search?.map(el => {
            let card = d.createRange().createContextualFragment(`
                <article class="card">
                    <p class="title">${el.Title}</p>
                    <p>Stock ${el.stocked ?'✔️' : '🚫' }</>
                    <p>$ ${el.Price}</p>
                </article>
            `)

            $$('.main-section')[1].appendChild(card)
        })

    } catch (err) {
        console.error('Error inesperdo ', err)
    }
}
