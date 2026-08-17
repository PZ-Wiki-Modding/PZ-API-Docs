/**
 * Initialize copy-to-clipboard functionality for attribute links
 */
function initAttributeLinkButtons() {
    // Find all attribute directives (dl.py.attribute)
    const attributeElements = document.querySelectorAll('dl.py.attribute');
    
    attributeElements.forEach(attrElement => {
        // Get the anchor ID directly from the dl element
        const elementId = attrElement.id;
        if (!elementId) return;
        
        // Find the dt (definition term) which contains the attribute name
        const dt = attrElement.querySelector('dt');
        if (!dt) return;
        
        // Create the link icon button
        const button = document.createElement('button');
        button.className = 'copy-link-btn';
        button.setAttribute('title', 'Copy link to this attribute');
        button.setAttribute('aria-label', 'Copy link to this attribute');
        button.innerHTML = `<svg class="link-icon" width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
            <path d="M7.657 6.247c.11-.33.576-.55.89-.49l4.885.856c.677.123 1.24.644 1.24 1.289v5.313c0 .668-.306 1.292-.764 1.697a2.25 2.25 0 01-1.449.574h-.5a.75.75 0 010-1.5h.5c.56 0 1.063-.208 1.419-.557.356-.349.578-.853.578-1.382V8.917c0-.1-.046-.147-.141-.154l-4.885-.856c-.12-.021-.191.04-.191.161V13a.75.75 0 01-1.5 0V7.16c0-.615.395-1.14.899-1.356z"/>
            <path d="M3 6a3 3 0 013-3h2.5a.75.75 0 010 1.5H6a1.5 1.5 0 00-1.5 1.5v7a1.5 1.5 0 001.5 1.5h7a1.5 1.5 0 001.5-1.5v-2.5a.75.75 0 011.5 0v2.5A3 3 0 0113 3H6a3 3 0 00-3 3v7a3 3 0 003 3h7a3 3 0 003-3v-2.5a.75.75 0 01-1.5 0v2.5A1.5 1.5 0 0113 9H6a1.5 1.5 0 01-1.5-1.5V6z"/>
        </svg>`;
        
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const baseUrl = window.location.origin + window.location.pathname;
            const fullLink = baseUrl + '#' + elementId;
            
            navigator.clipboard.writeText(fullLink).then(() => {
                // Show success feedback
                const originalHTML = button.innerHTML;
                button.innerHTML = '✓';
                button.classList.add('copy-link-copied');
                
                setTimeout(() => {
                    button.innerHTML = originalHTML;
                    button.classList.remove('copy-link-copied');
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy link:', err);
            });
        });
        
        // Insert button next to the attribute name
        dt.appendChild(button);
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAttributeLinkButtons);
} else {
    initAttributeLinkButtons();
}
