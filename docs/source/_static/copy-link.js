/**
 * Initialize copy-to-clipboard functionality for attribute links
 * 
 * Generated with AI help
 * Adjusted to my liking and optimized a bit
 */
function initAttributeLinkButtons() {
    // Find all attribute directives (dl.py.attribute)
    const attributeElements = document.querySelectorAll('dl.py.attribute');
    const buttons = []; // cache
    
    // for each attribute, we add a copy link button next to the attribute name
    // this is mostly a hack bcs I want to keep the nice visuals of attribute
    // directives, but they don't provide a copy link button by default
    attributeElements.forEach(attrElement => {
        // Get the anchor ID directly from the dl element
        const elementId = attrElement.id;
        if (!elementId) return;
        
        // Find the dt (definition term) which contains the attribute name
        const dt = attrElement.querySelector('dt');
        if (!dt) return;
        
        // creating the link icon button
        const button = document.createElement('button');
        button.className = 'copy-link-btn'; // see custom.css
        
        // hover label
        button.setAttribute('title', 'Copy link');

        // apparently for accessibility (screen readers)
        button.setAttribute('aria-label', 'Copy link'); 

        // see custom.css for styling
        button.innerHTML = '<img class="link-icon" src="/_static/anchor-link.svg" alt="Copy link" />';
        
        // on click we copy the link and show 
        // a small visual temporarily for feedback
        button.addEventListener('click', async (e) => {
            e.preventDefault();
            e.stopPropagation();

            const fullLink = window.location.href.split('#')[0] + '#' + elementId;

            let copySucceeded = false;
            try {
                await navigator.clipboard.writeText(fullLink);
                copySucceeded = true;
            } catch (err) {
                // console.error('Failed to copy link:', err);

                // fallback in case navigator.clipboard is not available or fails
                const textarea = document.createElement('textarea');
                textarea.value = fullLink;
                textarea.style.position = 'fixed';
                textarea.style.opacity = '0';
                document.body.appendChild(textarea);
                textarea.select();

                // copy to clipboard
                try {
                    document.execCommand('copy');
                    copySucceeded = true;
                } catch (fallbackErr) {
                    console.error('Fallback copy also failed:', fallbackErr);
                }

                textarea.remove();
            }

            // visual feedback for the copy
            if (copySucceeded) {
                const originalHTML = button.innerHTML;
                button.innerHTML = '<img class="success-icon" src="/_static/tick-mark.svg" alt="Copy link" />';
                // button.classList.add('copy-link-copied');

                setTimeout(() => {
                    button.innerHTML = originalHTML;
                    // button.classList.remove('copy-link-copied');
                }, 2000);
            }
        });
        
        // Insert button next to the attribute name
        dt.appendChild(button);
        buttons.push(button);
    });

    // hide the button if too far
    // this wasn't done with a hover because the button
    // would stay invisible until somehow the user hovered it
    // which is not intuitive
    let lastTime;
    document.addEventListener('mousemove', (e) => {
        // throttle for performance
        if (!lastTime) lastTime = Date.now();
        const now = Date.now();
        if (now - lastTime < 250) return;
        lastTime = now;

        // adjust opacity based on distance squared
        buttons.forEach(btn => {
            const rect = btn.getBoundingClientRect();
            const distanceSq = 
                Math.pow(e.clientX - rect.left - rect.width/2, 2) + 
                Math.pow(e.clientY - rect.top - rect.height/2, 2)
            ;
            btn.style.opacity = Math.max(0, 1 - (distanceSq / 22500));
        });
    });
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAttributeLinkButtons);
} else {
    initAttributeLinkButtons();
}
