<?php
/**
 * SocialEngine
 *
 * @category   Application_Extensions
 * @package    Touch
 * @copyright  Copyright Hire-Experts LLC
 * @license    http://www.hire-experts.com
 * @version    $Id: view.tpl 2011-04-26 11:18:13 mirlan $
 * @author     Mirlan
 */

?>
<script type="text/javascript">
window.addEvent('domready', function() {
	var options={
		prev_button: 'paginator-navigation-prev',
		next_button: 'paginator-navigation-next',
		media_photo: 'media_photo_next'
	}
	$('media_photo').addEvent('click', function(){
			en4.core.runonce.add(function(){
				Photobox.setOptions(options);

				if (Photobox.isOpen){
				 Photobox.show('media_photo');
				}
			});
	});
})();

  en4.core.runonce.add(function() {
  

    var taggerInstance = window.taggerInstance = new Tagger('media_photo_next', {
      'title' : '<?php echo $this->string()->escapeJavascript($this->translate('ADD TAG'));?>',
      'description' : '<?php echo $this->string()->escapeJavascript($this->translate('Type a tag or select a name from the list.'));?>',
      'createRequestOptions' : {
        'url' : '<?php echo $this->url(array('module' => 'core', 'controller' => 'tag', 'action' => 'add'), 'default', true) ?>',
        'data' : {
          'subject' : '<?php echo $this->subject()->getGuid() ?>'
        }
      },
      'deleteRequestOptions' : {
        'url' : '<?php echo $this->url(array('module' => 'core', 'controller' => 'tag', 'action' => 'remove'), 'default', true) ?>',
        'data' : {
          'subject' : '<?php echo $this->subject()->getGuid() ?>'
        }
      },
      'cropOptions' : {
        'container' : $('media_photo_next')
      },
      'tagListElement' : 'media_tags',
      'existingTags' : <?php echo Zend_Json::encode($this->tags) ?>,
      'suggestProto' : 'request.json',
      'suggestParam' : "<?php echo $this->url(array('module' => 'user', 'controller' => 'friends', 'action' => 'suggest', 'includeSelf' => true), 'default', true) ?>",
      'guid' : <?php echo ( $this->viewer()->getIdentity() ? "'".$this->viewer()->getGuid()."'" : 'false' ) ?>,
      'enableCreate' : <?php echo ( $this->canTag ? 'true' : 'false') ?>,
      'enableDelete' : <?php echo ( $this->canUntagGlobal ? 'true' : 'false') ?>
    });

    // Remove the href attrib while tagging
    var nextHref = $('media_photo_next').get('href');
    taggerInstance.addEvents({
      'onBegin' : function() {
        $('media_photo_next').erase('href');
      },
      'onEnd' : function() {
        $('media_photo_next').set('href', nextHref);
      }
    });
    
    var keyupEvent = function(e) {
      if( e.target.get('tag') == 'html' ||
          e.target.get('tag') == 'body' ) {
        if( e.key == 'right' ) {
          $('photo_next').fireEvent('click', e);
          //window.location.href = "<?php echo ( $this->nextPhoto ? $this->nextPhoto->getHref() : 'window.location.href' ) ?>";
        } else if( e.key == 'left' ) {
          $('photo_prev').fireEvent('click', e);
          //window.location.href = "<?php echo ( $this->previousPhoto ? $this->previousPhoto->getHref() : 'window.location.href' ) ?>";
        }
      }
    }
    window.addEvent('keyup', keyupEvent);
    
    // Add shutdown handler
    en4.core.shutdown.add(function() {
      window.removeEvent('keyup', keyupEvent);
    });
  });
  
   function showTags(){
  	$$('.tag_div').removeClass('tag_div_hidden');
  	$$('.tag_label').removeClass('tag_label_hidden');
  	window.he_show_message("Please rotate device if you don't see the tag on the picture", 'notice');
  }
  function hideTags(){
  	$$('.tag_div').addClass('tag_div_hidden');
  	$$('.tag_label').addClass('tag_label_hidden');
  }
</script>

<?php
$next_photo = $this->nextPhoto;
$prev_photo = $this->previousPhoto;
?>

<div class="touch-navigation">
	<div class="navigation-header navigation-paginator">
		<?php if ($this->album->count() > 1): ?>
			<span class="touch-navigation-paginator">
				<a  class="paginator-navigation" href="<?php echo $prev_photo->getHref(); ?>" id="paginator-navigation-prev"
						onclick="Touch.navigation.request($(this)); return false;">
					<img src="application/modules/Touch/themes/<?php echo $this->touchActiveTheme(); ?>/images/prev.png" alt="<?php echo $this->translate('Prev') ?>" />
				</a>

      <a class="paginator-navigation" href="<?php echo $next_photo->getHref(); ?>"  id="paginator-navigation-next"
					 onclick="Touch.navigation.request($(this)); return false;">
        <img src="application/modules/Touch/themes/<?php echo $this->touchActiveTheme(); ?>/images/next.png" alt="<?php echo $this->translate('Next') ?>" />
				</a>
			</span>
		<?php endif; ?>



		<div id="navigation-selector">
				<?php echo ( '' != trim($this->photo->getTitle()) ? $this->touchSubstr($this->photo->getTitle(), 25) : $this->translate('Untitled Photo')); ?>
		</div>
		<div class="navigation-body">
			<div id="navigation-items" style="display:none;">
				<div class="item active">
					<?php echo $this->htmlLink($this->photo, ( '' != trim($this->photo->getTitle()) ? $this->photo->getTitle() : $this->translate('Untitled Photo')), array("class" => "touchajax")); ?>
				</div>

				<div class="item">
					<?php echo $this->htmlLink($this->album, $this->translate('TOUCH_Back to Album'), array("class" => "touchajax")); ?>
				</div>
				<div class="item">
					<?php echo $this->htmlLink($this->album->getOwner(), $this->translate('%1$s\'s Profile', $this->album->getOwner()->getTitle()), array("class" => "touchajax")) ?>
				</div>
			</div>
		</div>
	</div>

	<div style="height:10px"></div>

	<div id="navigation_loading" style="display:none; text-align: center; vertical-align: middle;">
		<a class="loader"><?php echo $this->translate("Loading"); ?>...</a>
	</div>

	<div id="navigation_content">
		<div class="layout_content">
			<div class="album_photo_left">
						<?php echo $this->translate('Added %1$s', $this->timestamp($this->photo->modified_date)) ?>
			</div>

			<div class="album_photo_right">
				<?php echo $this->translate('TOUCH_Photo %1$s of %2$s',
						$this->locale()->toNumber($this->photoIndex + 1),
						$this->locale()->toNumber($this->album->count()))?>
				<div id="loading_photo"></div>
			</div>

			<div class="clr"></div>

			<div class='photo_view_container'>
				<div class='album_viewmedia_container photo' id='media_photo_div'>
					<a id='media_photo_next'  href='<?php echo $this->escape($next_photo->getHref()) ?>' onclick="return false;">
						<?php echo $this->htmlImage($this->photo->getPhotoUrl(), $this->photo->getTitle(), array(
							'id' => 'media_photo',
						)); ?>
					</a>
				</div>
                            
                                <div class="albums_viewmedia_info_tags" id="media_tags" style="display: none;">
                                  <?php echo $this->translate('Tagged:') ?>
                                </div>
                                  <div class="albums_viewmedia_info_footer">                            
                                <?php if ($this->viewer()->getIdentity()):?>
                            
                                <?php if( $this->canTag ): ?>
                                   <?php echo $this->htmlLink('javascript:void(0);', $this->translate('Add Tag'), array('onclick'=>'taggerInstance.begin();')) ?>
                                <?php endif; ?> 
                                
                              - <?php if( $this->canDelete ): ?>
					&nbsp;<?php echo $this->htmlLink(array('reset' => false, 'action' => 'delete'), $this->translate('Delete') . '<div style="display:none"> ' . $this->translate('TOUCH_this photo') . ' ?</div>', array('class' => 'touchconfirm redirect')) ?>
				<?php endif; ?>
                                
                              - <?php if( !$this->message_view && $this->viewer()->getIdentity() ):?>
					&nbsp;<?php echo $this->htmlLink(Array('module'=> 'activity', 'controller' => 'index', 'action' => 'share', 'route' => 'default', 'type' => 'album_photo', 'id' => $this->photo->getIdentity()), $this->translate("Share"), array('class' => 'smoothbox')); ?>
					- <?php echo $this->htmlLink('javascript:void(0);', $this->translate('Show All Tag'),array('onclick'=>'showTags();')) ?>
        - <?php echo $this->htmlLink('javascript:void(0);', $this->translate('Hide All Tag'),array('onclick'=>'hideTags();')) ?>
				<?php endif;?>
                                
                                <?php endif;?>
                                  </div>

                  <?php
                  if (Engine_Api::_()->getApi('settings', 'core')->getSetting('touch.album.rate-widget', 1)){ ?>
                        <?php echo $this->content()->renderWidget('touch.rate-widget') ?>

                  <?php } ?>
                
            </div>

            <?php echo $this->touchAction("list", "comment", "core", array("type"=>"album_photo", "id"=>$this->photo->getIdentity(), 'viewAllLikes'=>true)); ?>


        </div>
    </div>
</div>
