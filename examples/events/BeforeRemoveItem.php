<?php

declare(strict_types=1);

namespace Full\Qualified\Namespace;

use OxidEsales\GraphQL\Storefront\Basket\Event\BeforeRemoveItem;
use Symfony\Component\EventDispatcher\EventSubscriberInterface;

class DeveloperBeforeRemoveItemEventSubscriber implements EventSubscriberInterface
{
    public function handle(BeforeRemoveItem $event): BeforeRemoveItem
    {
        //get the user basket id from event
        $userBasketId = (string) $event->getBasketId();

        //get the user basket item id from event
        $basketItemId = (string) $event->getBasketItemId();

        //get the user basket item amount from event
        $amount = (float) $event->getAmount();

        //do something

        return $event;
    }

    public static function getSubscribedEvents()
    {
        return [
            'OxidEsales\GraphQL\Storefront\Basket\Event\BeforeRemoveItem' => 'handle'
        ];
    }
}
